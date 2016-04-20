import subprocess
import csv

cmd = "torcs"

p = subprocess.Popen(cmd,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)

for line in iter(p.stdout.readline, b''):
    print(line.rstrip())


