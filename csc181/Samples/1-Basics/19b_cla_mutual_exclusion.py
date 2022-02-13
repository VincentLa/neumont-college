"""
Demonstrates Command Line Arguments where you want "mutual exclusion"

That is, you have two arguments, and the user HAS to specify one or the other, but NOT both. 
"""

import argparse

parser = argparse.ArgumentParser(description='Put your description here')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-a', type=str, help='text to add to a file')
group.add_argument('-l', action='store_true', help='Use this switch to list file contents')

args = parser.parse_args()

a = args.a 
l = args.l

print(args.a)
print(l)
