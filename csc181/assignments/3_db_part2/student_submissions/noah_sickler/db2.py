import os
import json
import sys

#Create Json File

#Write to json file
def writeFile(data):
    with open("db.json", 'w') as f:
        f.write(json.dumps(data))
#read the file
def read():
    if not os.path.isfile("db.json"):
        with open("db.json", 'w') as f:
            print("Loading File...")
            json.dump([],f)
    with open('db.json', 'r') as f:
        return json.load(f)

def addPerson(firstName, lastName, phone, email):

    print("HELLO IM IN ADD PRSON")
    person = {"Firstname": firstName, "Lastname": lastName, "Phone-number": phone, "Email": email}
    data = read()

    data.append(person)

    print('data')
    writeFile(data)

    print(f"{firstName} {lastName} has been added!")

def findPerson(value):
    data = read()

    for entry in data:
        if entry['firstname'].lower() == value.lower() or entry['lastname'].lower() == value.lower():
            print(json.dumps(entry, indent=3))
            return

    print("User could not be found!!")

#Add a delete
def deleteUser(value):
    data = read()
    for entry in data:
        if entry['firstname'].lower() == value.lower() or entry['lastname'].lower() == value.lower():
            data.remove(entry)
            writeFile(data)
            firstName = entry['firstname']
            lastName = entry['lastname']
            print(f"{firstName} {lastName} has been deleted. ")
            return

def listUsers():
    data = read()
    for entry in data:
        print(json.dumps(entry, indent=2))

#add method

programisrunning = True
while programisrunning:

    #Get user input
    userInput=  input('Enter an option: \-a add person \n -l search \n -d delete a record \n -f search for a record \n -q Exit')
    userInput = userInput.split()

    print(userInput)

    #Give user options to do stuff
    if '-a' == userInput[0] and len(userInput) == 5:
        firstName, lastName, phone, email = userInput[1:]
        addPerson(firstName, lastName, phone, email)
    elif '-l' == userInput[0] and len(userInput) == 1:
        listUsers()
    elif '-f' == userInput[0] and len(userInput) == 2:
        value = userInput[1]
        findPerson(value)

    elif '-d' == userInput[0] and len(userInput) == 2:
        value = userInput[1]
        deleteUser
        (value)

    elif userInput[0] == '-q':
        #Find a way to quit
        programisrunning = False

    else:
        print('\nERROR: -f is used for first name. ')
        print('\n-l lists all records. ')
        print('\n-a Add name, phone & email.')
        print('\n-d with a users name and delete their record.')
