import argparse
from pathlib import Path
import json
from posixpath import split


parser = argparse.ArgumentParser(description='Put your description here')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-a', type=str, help='Add new record [fname] [lname] [phone] [email]')
group.add_argument('-l', action='store_true', help='Use this switch to list file contents')
group.add_argument('-f', help='find and show the first record that matches the search')
group.add_argument('-d', help='delete the first record that matches the search')
group.add_argument('-q', help='quit the CLI')

args = parser.parse_args()
a = args.a 
l = args.l
f = args.f
d = args.d
q = args.q

def write_to_file(a):
    path_to_file = 'db.json'
    path = Path(path_to_file)

    
    
    if path.is_file():
        # Adds line to file
        file = open('db.json', 'a')
        file.write(a)
        data_json = json.loads(a)
        file.close()
        print(str(data_json) + " added")
    else:
        # Writes files
        file = open('db.json', 'w')
        file.write(a)
        data_json = json.loads(a)
        file.close()
        print("new file created, " + str(data_json) + " added")
    
    print("done")
    
    
def read_file(l):
    # Reads file     
    string_json = json.dumps(write_to_file.data_json) # use json.dumps to convert json to a string
    print(string_json)
    file = open('data.json', 'r')
    content = file.read()
    file.close()
    print(content)
    
def find_file(f):
    # Finds the first record shown
    print("file found")
    
    
def delete_record(d):
    # deletes the first searched record
    print("record deleted")
    
def quit(q):
    # quits the CLI
    quit()          
    
if a != None:
    write_to_file(a)
elif l:
    try:
        read_file(l)
    except:
        print("File does not exist yet")
elif f:
    try:
        find_file(f)
    except:
        print("File not found")
elif d:
    try:
        delete_record(d)
    except:
        print("record not found")
else: 
    print('Please use proper args, example: \ndb -a "fname lname phone email": adds new record \ndb -l: lists all records \ndb -f search: finds one record \ndb -d search: deletes one record')

#I procrastinated too long and couldn't finish on time