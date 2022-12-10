#!/usr/bin/env python3
import os
import sys
import shutil
import argparse
description = ''' ./rm.py [OPTION]... [FILE]...
Remove (unlink) the FILE(s).\n'''
parser = argparse.ArgumentParser(description)
parser.add_argument('-r', '-R', '--recursive', action='store_true', default=False, required=False,  help='remove directories and their contents recursively')
parser.add_argument('input', nargs='*')
args = parser.parse_args()
for file in args.input:
    if os.path.isdir(file) and args.recursive:
        shutil.rmtree(os.path.abspath(file))
    elif os.path.isfile(file):
       os.remove(os.path.abspath(file))


