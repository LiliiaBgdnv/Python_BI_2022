  GNU nano 4.8                                                                    wc.py                                                                              #!/usr/bin/env python3
import sys
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType(), default=sys.stdin, nargs='?')
parser.add_argument('-l', '--lines', action='store_true', default=False, help='print the newline counts')
parser.add_argument('-w', '--words', action='store_true', default=False, help='print the word counts')
parser.add_argument('-c', '--count', action='store_true', default=False, help='print the byte counts')
args = parser.parse_args()
chars = words = lines = 0
output=[]
if args.count:
    for line in args.file:
        chars += len(line)
    output.append(str(chars))
    output.append(args.file.name)
if args.words:
    for line in args.file:
        words += len(line.split())
    output.append(str(words))
    output.append(args.file.name)
if args.lines:
    for line in args.file:
        lines += 1
    output.append(str(lines))
    output.append(args.file.name)
output.append('\n')
sys.stdout.write(' '.join(output))
