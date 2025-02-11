#!/usr/bin/env python3
import argparse, sys
from src import cleaners

# minimal CLI dispatcher

def main(argv=None):
    p = argparse.ArgumentParser(prog='dclean', description='Small data cleaning helpers')
    sub = p.add_subparsers(dest='cmd', required=True)

    ptrim = sub.add_parser('trim', help='Trim whitespace for each line')
    ptrim.add_argument('-i','--infile', type=argparse.FileType('r'), default='-')

    punique = sub.add_parser('unique', help='Unique lines preserving order')
    punique.add_argument('-i','--infile', type=argparse.FileType('r'), default='-')

    args = p.parse_args(argv)
    if args.cmd == 'trim':
        data = args.infile.read().splitlines()
        for line in cleaners.trim_lines(data):
            print(line)
    elif args.cmd == 'unique':
        data = args.infile.read().splitlines()
        for line in cleaners.unique_lines(data):
            print(line)

if __name__ == '__main__':
    main()
