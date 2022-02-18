    # Requirements
    # The database will append whatever comes after '-a' in the command line arguments to a text file called 'data.txt'
    # Use the '-l' to list the contents of the text file
    # If the user passes in too few or incorrect arguments, print
    # the proper usage for the application on the screen and exit the application so they can try again.
    # If the database text file (in this case 'data.txt') doesn't exist yet use a try/except to
    # handle this edge case. In particular, if the file doesn't exist, and "-l" is passed, print a message
    # that says "File does not exist yet". If "-a" is passed, create the file, add the content to the text file, and say "new file created, content added".
    # When adding something to the text file and the text file already exists, print a message that says, "content added."

import argparse
import textwrap
import os.path
import sys

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

parser = MyParser(prog="Database",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
        Command Line Database Application
        ---------------------------------
            You must use one argument
                provided below
        '''))
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-a', type=str, help='text to add to a file')
group.add_argument('-l', action='store_true', help='Use this switch to list file contents')


args = parser.parse_args()

if args == None:
    parser.print_help()

a = args.a
l = args.l

if a != None:
    file_exists = os.path.exists('data.txt')
    if file_exists:
        with open('data.txt', 'a') as file:
            file.write("\n" + a)
            print("Content Added")
    else:
        with open('data.txt', 'w') as file:
            file.write(a)
            print("New File Created, Content Added")

if l == True:
    try:
        with open('data.txt', 'r') as file:
            contents = file.read()
            print(contents)
    except:
        print("The file does not exist yet.")
