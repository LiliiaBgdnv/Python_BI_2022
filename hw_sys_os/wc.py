#!/usr/bin/env python3
import sys
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType(), default=sys.stdin, nargs='?')
parser.add_argument('-l', '--lines', action='store_true', help='print the newline counts')
parser.add_argument('-w', '--words', action='store_true', help='print the word counts')
parser.add_argument('-c', '--count', action='store_true', help='print the byte counts')
args = parser.parse_args()
chars = words = lines = 0
output=[]
for line in args.file:
    words += len(line.split())
    lines += 1
if args.lines:
    output.append(str(lines))
if args.words:
    output.append(str(words))
if args.count:
    output.append(str(os.path.getsize(os.path.abspath(args.file.name))))
output.append(args.file.name)
output.append('\n')
sys.stdout.write(' '.join(output))
