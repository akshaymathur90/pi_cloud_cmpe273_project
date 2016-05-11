#!/usr/bin/python

print "hello world"
#import netifaces as ni
import requests
import datetime
import json
import time
import os

print "Script starting"




def test_post(url):
    post_url = "%s/directory" % url
    try:
        #ip1 = ni.ifaddresses('eth0')[2][0]['addr']
        f = os.popen('ifconfig eth0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
        your_ip=f.read()
        ip1 = your_ip.strip()
        print ip1
        payload = {
            "role": "master",
            "ip": ip1
        }
        r = requests.post(post_url, data=json.dumps(payload))
        if r.status_code == 201:
            d = datetime.datetime.now()
            print "POST Check successful. Time: %s" % d
        else:
            print "POST incorrect. Not working as expected."
    except requests.exceptions.ConnectionError:
        print "Server not running on %s" % url
        exit()

url = 'http://54.215.224.150:8080'
print "trying post in the next 30 sec.."
time.sleep(60)
print "calling test_post"
test_post(url)
print "called test_post"
