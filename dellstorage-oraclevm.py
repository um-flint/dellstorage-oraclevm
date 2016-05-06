#!/usr/bin/python

import requests
import json
import base64
import ConfigParser

#taken from the Oracle VM Web Services API Developer's Guide
def check_manager_state(baseUri,s):
    while True:
        r=s.get(baseUri+'/Manager')
        manager=r.json()
        if manager[0]['managerRunState'].upper() == 'RUNNING':
            break

        time.sleep(1)
    return

def main():
    config = ConfigParser.ConfigParser()
    config.readfp(open('dellstorage-oraclevm.cfg'))
    dellusername = config.get('dell','username')
    dellpassword = config.get('dell','password')
    dellUri = config.get('dell','baseUri')
    ovmusername = config.get('ovm','username')
    ovmpassword = config.get('ovm','password')
    ovmUri = config.get('ovm','baseUri')

    dells=requests.Session()
    dells.headers.update({'Accept': 'application/json', 'Content-Type': 'application/json', 'x-dell-api-version': '2.2'})
    dells.verify=False #disable once we get a real cert

    ovms=requests.Session()
    ovms.auth=(ovmusername, ovmpassword)
    ovms.headers.update({'Accept': 'application/json', 'Content-Type': 'application/json'})
    check_manager_state(ovmUri,ovms)

    dellauth = {'Authorization': 'Basic ' + base64.b64encode(dellusername + ':' + dellpassword), 'Content-Type': 'application/json', 'x-dell-api-version': '2.2'}
    r=s.post(dellUri+'/ApiConnection/Login','{}',headers=dellauth)
         
    r=s.post(dellUri+'/ApiConnection/Logout','{}')

    return

if __name__ == '__main__': 
    main()
