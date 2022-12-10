#!/usr/bin/env python3
import sys
import argparse
description = ''' sort [OPTION]... [FILE]...
  or:  sort [OPTION]... --files0-from=F
Write sorted concatenation of all FILE(s) to standard output.

With no FILE, or when FILE is -, read standard input.

Mandatory arguments to long options are mandatory for short options too.'''
parser = argparse.ArgumentParser(description)
parser.add_argument('file', nargs='?', type=argparse.FileType(), default=sys.stdin)
args = parser.parse_args()
for line in sorted(args.file):
    sys.stdout.write(line)
