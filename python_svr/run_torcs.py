import subprocess
import csv
import sys
import json

import publisher as pub
import time
import zmq

def main():
	if len(sys.argv) == 1: # no args
		cmd = "torcs"
	elif sys.argv[1] == 'bot':
		cmd = ["torcs", "-r", "/vagrant/torcs-1.3.6/src/raceman/quickrace.xml"]
		# start the pyclient
		runserver = ["python", "/vagrant/python_svr/pyclient.py"]
		subprocess.Popen(runserver, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	# Run command
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	# ZMQ setup
	ip = "127.0.0.1"
	port = 8690
	list_of_topics = ['simulator=']
	ZMQp = pub.Publisher(ip, port, list_of_topics)

	# Print stdout buffer
	for line in iter(p.stdout.readline, b''):
		pyout = {}
		splitline = line.split('\t')
		for info in splitline:
			nameValue = info.split(':')
			if(len(nameValue) == 2):
				pyout[nameValue[0]] = nameValue[1]
		jsonout=json.dumps(pyout)
		#print(jsonout)
		ZMQp.send_message('simulator=', jsonout)

if __name__ == "__main__":
	main()
