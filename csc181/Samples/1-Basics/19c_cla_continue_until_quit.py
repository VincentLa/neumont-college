"""
Another CLA example where you can allow the user to issue several command line arguments until "quit"
"""
import argparse
from argparse import Action


class StopAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        # Do whatever actions you want
        if values:
            print("Exiting")
            exit(0)


parser = argparse.ArgumentParser(description='Put your description here')
parser.add_argument('-add', type=str, help='Add a new record')
parser.add_argument('-list', action='store_true', required=False, help='Use this switch to list file contents')
parser.add_argument('-find', type=str, help='find and show the first record that matches the search')
parser.add_argument('-delete', type=str, help='delete the first record that matches the search')
parser.add_argument('quit', nargs='?', action=StopAction, default=False)

while True:
    args = parser.parse_args(input("enter arguments: ").split())
    print(args.add, args.list, args.find, args.delete)

    # Continue with the rest of your code here