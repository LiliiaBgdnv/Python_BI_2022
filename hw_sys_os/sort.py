#!/usr/bin/env python3
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType(), default=sys.stdin)
args = parser.parse_args()
for line in sorted(args.file):
    print(line, end='')
