#!/usr/bin/env python3
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='?', type=argparse.FileType(), default=sys.stdin)
args = parser.parse_args()
for line in sorted(args.file):
    sys.stdout.write(line)
