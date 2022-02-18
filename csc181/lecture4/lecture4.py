import argparse

parser = argparse.ArgumentParser(description='Put your description here')
parser.add_argument('-a', type=str, required=False, help='text to add to a file')
parser.add_argument('-l', action='store_true', required=False, help='Use this switch to list file contents')

args = parser.parse_args()

a = args.a 
l = args.l

print(args.a)
print(l)
