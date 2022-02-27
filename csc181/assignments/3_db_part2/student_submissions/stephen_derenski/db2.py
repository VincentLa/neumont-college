import argparse
import textwrap
import os.path
import sys
import json

TEXTDOC = 'data.json'

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()

parser = MyParser(prog="Database",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
        Command Line Database Application
        ---------------------------------
            You must use one argument
                provided below
        '''))
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-a', dest='add', nargs=4, type=str, metavar=('fname','lname','phone','email'), help='Adds new record')
group.add_argument('-l', dest='list', action='store_true', help='Lists all records')
group.add_argument('-f', dest='find', nargs=1, type=str, metavar=('search'), help='Finds one record')
group.add_argument('-d', dest='delete', nargs=1, type=str, metavar=('search'), help='Deletes one record')
group.add_argument('-q', dest='quit', action='store_true', help='Quits Application')

args = parser.parse_args()

a, l, f, d, q = args.add, args.list, args.find, args.delete, args.quit



#------------------------------------------------------------------

def writingJson(textDoc, typeE, dict):
    with open(textDoc, typeE) as json_file:
        json.dump(dict, json_file, indent=4, separators=(", ",": "))

def readingJson(textDoc):
    with open(textDoc, 'r') as file:
        return json.loads(file.read())


LIST_OF_KEYS = ['fname','lname','phone','email']

# Add Record
if a != None:
    dictOfPerson = dict(zip(LIST_OF_KEYS, a))
    file_exists = os.path.exists(TEXTDOC)
    if file_exists:
        listJson = readingJson(TEXTDOC)
        listJson.append(dictOfPerson)
        writingJson(TEXTDOC, 'w', listJson)
        print(listJson[-1]['fname'] + ' '+ listJson[-1]['lname'] + " was added.")
    else:
        listJson = []
        listJson.append(dictOfPerson)
        print(listJson)
        writingJson(TEXTDOC, 'w', listJson)
        print("New File Created, " + listJson[-1]['fname'] + ' '+ listJson[-1]['lname'] + " was added.")

try:
    if l == True or f != None or d != None:
        contents = readingJson(TEXTDOC)
        breakLoop = False
        for k in range(0, len(contents)):
            print()
            if breakLoop == True:
                break
            for v in LIST_OF_KEYS:
                # Listing out the records
                if l == True:
                    print(contents[k][v])

                # Find a record
                elif f != None:
                    if contents[k][v].lower() == f[0].lower():
                        [print(contents[k][t]) for t in LIST_OF_KEYS]

                # Delete a record
                elif d != None:
                    if contents[k][v].lower() == d[0].lower():
                        print(contents[k]['fname'] + ' '+ contents[k]['lname'] + " was removed.")
                        contents.pop(k)
                        writingJson(TEXTDOC, 'w', contents)
                        breakLoop = True
                        break
            print()


except:
    print("An issue happened...")
