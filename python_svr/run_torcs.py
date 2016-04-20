import subprocess
import csv
import sys


def main():
	if len(sys.argv) == 1: # no args
		cmd = "torcs"
	elif sys.argv[1] == 'human':
		cmd = "torcs"
		# todo run custom xml that selects the human player
	elif sys.argv[1] == 'bot':
		cmd = "torcs -r /vagrant/torcs-1.3.6/src/raceman/quickrace.xml"
		# start the pyclient

	# Run command
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	
	# Print stdout buffer
	for line in iter(p.stdout.readline, b''):
	    print(line.rstrip())

if __name__ == "__main__":
	main()
