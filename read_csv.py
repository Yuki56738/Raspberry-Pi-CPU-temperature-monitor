#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import sys

try:
  f = open(sys.argv[1], "r")
except:
    print(f"{sys.argv[0]} <csv file name>")
    sys.exit(1)
f2 = open("tmp.txt", "w")

i = 0
for x in f:
    x = x.replace("temp=", "")
    x = x.replace("'C", "")
    f2.write(x)
    print(x, end="")
    i = i + 1
print("---------")
f2.close()
f.close()

df = pd.read_csv("tmp.txt")
print(df)
x = df[df.keys()[0]]
y = df[df.keys()[1]]

plt.xlabel(df.keys()[0])
plt.ylabel(df.keys()[1])

plt.plot(x, y, linestyle="solid", marker="o")
plt.show()
