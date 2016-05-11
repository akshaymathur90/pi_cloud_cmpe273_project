"""
Script to test connection.go.
"""
import netifaces as ni
try:
    import requests
    import datetime
    import json
    import time
except Exception as e:
    print "Requests library not found. Please install it. \nHint: pip install requests"

payload = {
    "role": "master",
    "ip": ""
}


def test_get(url):
    get_url = "%s/directory/%s" % (url, payload['role'])
    print get_url
    r = requests.get(get_url)
    if r.status_code == 200:
        d = r.json()
        print d["ip"]
        registerToController(d["ip"])
    else:
        print "GET check failed"

def registerToController(ip):
	reg_url = "http://%s:5000/registerworker" %(ip)
	print reg_url
	myip = ni.ifaddresses('eth0')[2][0]['addr']
	print myip
	res = requests.post(reg_url, json={"IP":myip})
	print res
	if res.ok:
		print res.json()

#url = raw_input("Enter the url without trailing slash. Ex: http://localhost:3000:\n")
url = 'http://54.215.224.150:8080'
time.sleep(30)
test_get(url)
