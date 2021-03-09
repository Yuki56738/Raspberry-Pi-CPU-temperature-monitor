#!/usr/bin/python3
import subprocess
import time
import datetime
import csv
import sys

cmd=["vcgencmd", "measure_temp"]

global pr
#global f
#global w
#f=open("out.csv","w")
#w=csv.writter(f)
#global write
global fl
fl=open('out.txt','w')
#write=csv.writter('out.csv')
while True:
  try:
    pr = subprocess.run(cmd, stdout=subprocess.PIPE)
    print(f"{datetime.datetime.now()}: {pr.stdout.decode('utf8')}")
    fl.write(str(datetime.datetime.now()).rstrip()+"," +pr.stdout.decode('utf8').rstrip())
    fl.write('\n')
    time.sleep(1)
  except KeyboardInterrupt:
      print("stop!")
      fl.close()
      sys.exit(0)
