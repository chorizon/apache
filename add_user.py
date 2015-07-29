#!/usr/bin/python3

#This script work with systemd in debian jessie.

import sys
import subprocess
import argparse
import platform

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

if subprocess.call("sudo useradd --user="+args.user+" --password="+args.password+" --directory="+args.hostname,  shell=True) > 0:
	sys.exit(1)

#Create the directories in apache and restart.



#Create the quota if defined.

