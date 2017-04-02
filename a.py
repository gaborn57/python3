#! /usr/bin/env python3

import argparse

parser=argparse.ArgumentParser()

parser.add_argument("-v", "--verbose", help="display more informations", action="store_true")
parser.add_argument("-s", "--srv", help="to specify one or more servers. For more srv, use: -s \"srv1 srv2 srv3...\"", type=str)
parser.add_argument("-f", "--file", help="specify a source file. Each line containing a server name")

parser.parse_args()
