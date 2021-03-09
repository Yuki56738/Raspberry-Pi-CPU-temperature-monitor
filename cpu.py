#!/usr/bin/python3
import subprocess
import time
import datetime
import csv
import pandas as pd
import os

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
    #w.csv.writter(f)
    #w.writerow([datetime.datetime.now(),pr.stdout.decode('utf8')])
    ##df=pd.DataFrame([str(datetime.datetime.now()).rstrip(), pr.stdout.decode('utf8').rstrip()])
    ##df.to_csv('out.csv')
    fl.write(str(datetime.datetime.now()).rstrip()+"," +pr.stdout.decode('utf8').rstrip())
    fl.write('\n')
    time.sleep(1)
  except KeyboardInterrupt:
      print("stop!")
      fl.close()
      os.exit(0)
