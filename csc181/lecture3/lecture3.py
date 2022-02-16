import argparse

parser = argparse.ArgumentParser(description='Put your description here')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-a', type=str, help='text to add to a file')
group.add_argument('-l', action='store_true', help='Use this switch to list file contents')

args = parser.parse_args()

a = args.a 
l = args.l

if len(a) > 0:
    """this means the user passed a string"""
    # ADd the string to the file
elif l == True:
    print("list the contents of the file")
    # list the contents of the file