#! /usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 2 -*-

import sys

# params should only be integer
try:
  array = [ int(x) for x in sys.argv[1:] ]
except Exception as error:
  print("You should only give integer as parameters\n", error)
  sys.exit(1)

def BubbleSort(tableau):

  swaps = 0
  end = len(tableau) - 1

  echange = True
  while echange == True:
    print('End is now '+str(end))
    i = 0
    echange = False
    while i < end:
      if tableau[i] > tableau[i+1]:
        sys.stdout.write("{:>3d} <--> {:>3d}  ".format(tableau[i], tableau[i+1]))
        tmp = tableau[i]
        tableau[i] = tableau[i+1]
        tableau[i+1] = tmp
        echange = True
        swaps += 1
        sys.stdout.write("{}\n".format(tableau))
      i += 1
    end = end - 1
    i = 0
  print('Exiting because there were no value swapping')
  print(tableau)
  print('Nb of swaps: {}'.format(swaps))

if __name__ == '__main__':
  BubbleSort(array)
