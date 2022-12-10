#!/usr/bin/env python3
import sys
import os
import argparse
description = ''' ./wc.py [OPTION]... [FILE]...
  or:  ./wc.py [OPTION]... --files0-from=F
Print newline, word, and byte counts for each FILE, and a total line if
more than one FILE is specified.  A word is a non-zero-length sequence of
characters delimited by white space.\n

With no FILE, or when FILE is -, read standard input.\n'''
parser = argparse.ArgumentParser(description)
parser.add_argument('file', type=argparse.FileType(), default=sys.stdin, nargs='?')
parser.add_argument('-l', '--lines', action='store_true', help='print the newline counts')
parser.add_argument('-w', '--words', action='store_true', help='print the word counts')
parser.add_argument('-c', '--bytes', action='store_true', help='print the byte counts')
args = parser.parse_args()
words = lines = 0
output=[]
for line in args.file:
    words += len(line.split())
    lines += 1
if args.lines:
    output.append(str(lines))
if args.words:
    output.append(str(words))
if args.bytes:
    output.append(str(os.path.getsize(os.path.abspath(args.file.name))))
output.append(args.file.name)
output.append('\n')
sys.stdout.write(' '.join(output))
