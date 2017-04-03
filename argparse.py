#! /usr/bin/env python3

import argparse,sys

parser=argparse.ArgumentParser()

parser.add_argument("-v", "--verbose", help="display more informations", action="store_true")
parser.add_argument("-s", "--srv", help="to specify one or more servers. For more srv, use: -s \"srv1 srv2 srv3...\"", type=str)
parser.add_argument("-f", "--file", help="specify a source file. Each line containing a server name")

args=parser.parse_args()
servers=[]
if args.srv:
  for srv in args.srv.split(' '):
    if srv not in servers:
      servers.append(srv)
      if args.verbose:
        print("Added from srv option: "+srv)

if args.file:
  SRC=open(args.file, 'r')
  while 1:
    line=SRC.readline()
    if line=='':
      break
    line=line.rstrip('\n')
    if line not in servers:
      servers.append(line)
      if args.verbose:
        print("Added from file      : "+line)
  SRC.close()

if not (args.srv or args.file):
  sys.stderr.write("--srv or --file is needed. Exiting\n")
  sys.exit(1)

if len(servers)==0:
  sys.stderr.write('The provided arguments doesn\'t allow me to generate a server list. Exiting\n')
  sys.exit(2)

# à améliorer peut-être:
# --srv et --file : au moins un des deux est obligatoire


