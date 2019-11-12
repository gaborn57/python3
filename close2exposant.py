#! /usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 2 -*-

import sys
import math

val = input("Enter an integer\n")
try:
  int(val)
except:
  sys.stderr.write("The provided value is not an integer")
  sys.exit(1)

val = int(val)
minimum = val
for i in range(2, int(math.sqrt(val))+1):
  for j in range(2, int(math.sqrt(val))+1):
    if i**j > val:
      delta = val - last
      if delta <= minimum:
        minimum = delta
        vali = i
        valj = j-1
      break
    last = i**j

print("The exposant {}^{} is the closer to {}".format(vali, valj, val))
