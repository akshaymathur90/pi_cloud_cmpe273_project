# project/__init__.py

from flask import Flask, request, jsonify, json, session, render_template, json
from fabric.api import env,run,execute,hosts
from flask.ext.bcrypt import Bcrypt
from flask.ext.sqlalchemy import SQLAlchemy
import fabfile
import sqlite3
import modifyHAProxy
import databaseConn
from subprocess import call
from project.config import BaseConfig



# config

app = Flask(__name__)
app.config.from_object(BaseConfig)


bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
from project.models import User


# routes


@app.route('/api/register', methods=['POST'])
def register():
    json_data = request.json
    user = User(
        username = json_data['username'],
        email=json_data['email'],
        password=json_data['password']
    )
    try:
        db.session.add(user)
        db.session.commit()
        status = 'success'
    except:
        status = 'this user is already registered'
    db.session.close()
    return jsonify({'result': status})


@app.route('/api/login', methods=['GET','POST'])
def login():
    json_data = request.json
    u_id =''
    user = User.query.filter_by(email=json_data['email']).first()
    if user and bcrypt.check_password_hash(
            user.password, json_data['password']):
        session['logged_in'] = True
        session['uid'] = user.id
        u_id = user.id
        status = True
    else:
        status = False

    return jsonify({'result': status,'uid':u_id})

#@app.route('/')
#def index():
 #   return app.send_static_file('AddApp.html')
@app.route('/')
def index():
    return app.send_static_file('index.html')


#@app.route('/register', methods=['GET', 'POST'])
#def register():
  #  pass

@app.route('/api/logout', methods=['GET', 'POST'])
def logout():
     session.pop('logged_in', None)
     session.pop('uid', None)
     return jsonify({'result': 'success'})

@app.route('/api/status')
def status():
    if session.get('logged_in'):
        if session['logged_in']:
            return jsonify({'status': True})
    else:
        return jsonify({'status': False}) 


@app.route('/api/getapps',methods=['GET'])
def getapp():
    if session.get('uid'):
        if session['uid']:
           
            userid = session['uid']
            results = databaseConn.select_apps(userid)
            results["status"] = True
#            sushi = {"apps":[
#                    { "name": 'Cali Roll', "fish": 'Crab', "tastiness": 2 },
#                    { "name": 'Philly', "fish": 'Tuna', "tastiness": 4 },
#                    { "name": 'Tiger', "fish": 'Eel', "tastiness": 7 },
#                    { "name": 'Rainbow', "fish": 'Variety', "tastiness": 6 }
#                  ],
#                  "status":True
#                }
      
#            print json.dumps(results)
            return json.dumps(results)
    else:
        return jsonify({'status': False})         
            
@app.route('/registerworker',methods=['POST'])
def registerWorker():
	content = request.json
	print content['IP']
	# Insert in DB
	databaseConn.add_worker(content['IP'])
	return json.dumps({'html':'<span>All fields good !!</span>'})
			
@app.route('/newapp',methods=['POST'])
def signUp():
    appName = request.form['inputAppName']
    gitURL= request.form['inputGitURL']
    
    check = databaseConn.check_dups(appName)
    if check>1:
    	return json.dumps({'html':'Duplicate App Name'})
    if check==1:
        print "app exists re deploying"
        ipport = databaseConn.get_IP_port(appName)
        ipport=ipport.split(':')
        print "IP is = "+ipport[0]
        print "Port is = "+ipport[1]
        fabfile.install(gitURL,ipport[0],ipport[1])
    	return json.dumps({'html':'In database already.'})
    	
    workerip=databaseConn.get_workerIP()
    print "Worker iP from db = "+workerip
    
    port = databaseConn.get_availablePorts(workerip)
    
    if port == -1:
    	return json.dumps({'html':'All ports are in use.'})
    fabfile.install(gitURL,workerip,port)
    
    #Input data to DB
    
    
    aclName='is_'+appName
    pathName='/'+appName
    backendName='backend_'+appName
    serverName='serv_'+appName
    databaseConn.add_instance(appName, pathName, workerip, int(port),session['uid'])
    print gitURL,appName
    
    #Modify HA Proxy
    modifyHAProxy.insertNewApp(aclName, pathName, backendName, serverName, workerip, port)
    call(['haproxy -D -f /home/pi/pi_cloud_cmpe273_project/config.cfg -p /home/pi/pi_cloud_cmpe273_project/haproxy.pid -sf $(cat /home/pi/pi_cloud_cmpe273_project/haproxy.pid)'],shell=True)
    return json.dumps({'html':'<span>All fields good !!</span>'})

#if __name__ == "__main__":
 #   app.run(debug=True)		

