#!/usr/bin/python3

#This script work with systemd in debian jessie.

import sys
import subprocess
import argparse
import platform
import json

sys.path.append('../')

from libraries.functions.cmkdir import cmkdir

pyv=platform.python_version_tuple()

if pyv[0]!='3':
	print('Need python 3 for execute this script')
	sys.exit(1)

parser = argparse.ArgumentParser(description='Script for download chorizon.')

parser.add_argument('--hostname', help='Principal hostname of the new webhosting account', required=True)

parser.add_argument('--user', help='Username of the new webhosting account', required=True)

parser.add_argument('--password', help='Password of the new webhosting account', required=True)

parser.add_argument('--quota', help='Username of the new webhosting account', required=False)

args = parser.parse_args()

#Create the user.

if subprocess.call("sudo python3 ../libraries/scripts/users/useradd.py --user="+args.user+" --password="+args.password+" --directory=/home/"+args.user,  shell=True) > 0:
	
	sys.exit(1)

#Create the directories in apache and restart.

if not cmkdir('/etc/apache2/sites-enabled/'+args.hostname, args.user, args.user) :
	print(json.JSONEncoder().encode([0, 'CANNOT CREATE DIR']))
	sys.exit(1)

#Create the quota if defined.

