
import argparse
def add(value) :
    with open('data.txt', 'a') as file:
        file.write(value + "\n")


def read() :
    with open ('data.txt') as file:
        return file.readlines()
    
parser = argparse.ArgumentParser(description='Files And Text')
parser.add_argument('-a', type=str, required=False, help='text to add to a file')
parser.add_argument('-l', action='store_true', required=False, help='Use this switch to list file contents')
args = parser.parse_args()
if(args.a):
    a=args.a
    add(a)
elif(args.l):
    l = args.l
    print(read())

