#!/usr/bin/env python3
import os
import sys
import shutil
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-r', action='store_true', default=False, required=False,  help='delete an entire directory tree')
parser.add_argument('input', help='input file or directory which you wont delete')
args = parser.parse_args()
if os.path.isdir(args.input) and args.r:
    shutil.rmtree(os.path.abspath(args.input))
elif os.path.isfile(args.input):
    os.remove(os.path.abspath(args.input))

