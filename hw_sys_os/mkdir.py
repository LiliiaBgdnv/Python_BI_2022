#!/usr/bin/env python3
import os
import argparse
description = '''  mkdir [OPTION]... DIRECTORY...
Create the DIRECTORY(ies), if they do not already exist.'''
parser = argparse.ArgumentParser(description)
parser.add_argument('path', nargs='*')
parser.add_argument('-p', '--parents', help='no error if existing, make parent directories as needed')
args = parser.parse_args()
if args.parents:
    for name in args.path:
        if not os.path.exists(name, exist_ok=True):
            os.makedirs(name)
else:
    for name in args.path:
        if not os.path.exists(name, exist_ok=False):
            os.makedirs(name)
