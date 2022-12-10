#!/usr/bin/env python3
import os
import argparse
def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)
description = ''' ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

Mandatory arguments to long options are mandatory for short options too.'''
parser = argparse.ArgumentParser(description)
parser.add_argument('-a', '--all',  action='store_true',  default=False, required=False, help='do not ignore entries starting with .')
parser.add_argument('some_dir', type=dir_path, nargs='?')
args = parser.parse_args()
if args.all and args.some_dir:
    list_dir = sorted(os.listdir(path=args.some_dir))
    sys.stdout.write('.\n')
    sys.stdout.write('..\n')
elif args.all:
    sys.stdout.write('.\n')
    sys.stdout.write('..\n')
    list_dir = sorted(os.listdir(path='.'))
elif args.some_dir:
    list_dir = sorted((f for f in os.listdir(path=args.some_dir) if not f.startswith('.')))
else:
    list_dir = sorted((f for f in os.listdir() if not f.startswith('.')))
sys.stdout.write('\n'.join(list_dir))
