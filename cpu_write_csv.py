#!/usr/bin/python3
import subprocess
import time
import datetime
import csv
import sys

cmd=["vcgencmd", "measure_temp"]

global pr
global write
global fl
file_name = f"{datetime.datetime.now()}.txt"
fl=open(file_name,'w')
#write=csv.writter('out.csv')
while True:
  try:
    pr = subprocess.run(cmd, stdout=subprocess.PIPE)
    print(f"{datetime.datetime.now()}: {pr.stdout.decode('utf8')}")
    fl.write(str(datetime.datetime.now()).rstrip()+"," +pr.stdout.decode('utf8').rstrip())
    fl.write("\n")
    time.sleep(1)
  except KeyboardInterrupt:
      print("stop!")
      fl.close()
      sys.exit(0)
