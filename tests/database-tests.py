#!/usr/bin/env python3
import requests
import json
import time
import config

url = "{}{}".format(config.read_config("url"),"/databases")

while True:
 r = requests.get(url, auth=('x', 'x'))
 print(r.status_code)
 if (r.status_code < 400):
  for x in r.json():
    print ("removing", x['id'],"databasename = " ,x['databasename'])
    x = requests.delete("%s/%s" % (url,x['id']), auth=('x', 'x'))
    #for key in x.keys(): print(key)

 print ("Adding a new database")
 y = requests.post(url, json = {"domain_id":"1" , "databasename":"x", "username": "x", "password":"x"}, auth=('x', 'x'))
 print("pausing for 10secs")
 time.sleep(10)