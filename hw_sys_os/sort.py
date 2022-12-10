#!/usr/bin/env python3
import sys
import argparse
description = ''' ./sort.py [OPTION]... [FILE]...
  or:  ./sort.py [OPTION]... --files0-from=F
Write sorted concatenation of all FILE(s) to standard output.\n

With no FILE, or when FILE is -, read standard input.\n

Mandatory arguments to long options are mandatory for short options too.\n'''
parser = argparse.ArgumentParser(description)
parser.add_argument('file', nargs='?', type=argparse.FileType(), default=sys.stdin)
args = parser.parse_args()
for line in sorted(args.file):
    sys.stdout.write(line)
