#!/usr/bin/env python3
import sys
import argparse
description = ''' cat [OPTION]... [FILE]...
Concatenate FILE(s) to standard output.
'''
parser = argparse.ArgumentParser(description)
parser.add_argument('input', nargs='*',  type=argparse.FileType(), default=sys.stdin)
args = parser.parse_args()
for file in args.input:
    for line in file:
        sys.stdout.write(line)
