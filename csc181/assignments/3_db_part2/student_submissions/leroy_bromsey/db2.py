import json
import os
import sys

def writeData(data):
    with open("db.json", 'w') as f:
        f.write(json.dumps(data))

def readData():
    if not os.path.isfile("db.json"):
        with open("db.json", 'w') as f:
            print("Initializing your file...")
            json.dump([],f)

    with open('db.json', 'r') as f:
        return json.load(f)

def addCommand(fName, lName, phone, email):
    person = {"Firstname": fName, "Lastname": lName, "Phone number": phone, "email": email}
    data = readData()
    data.append(person)
    writeData(data)
    print(f"added {fName} {lName}!")

def findCommand(value):
    data = readData()

    for entry in data:
        if entry['Firstname'].lower() == value.lower() or entry['Lastname'].lower() == value.lower():
            print(json.dumps(entry, indent=2))
            return

    print("no user with that name was found")

findCommand("Leroy")

def listCommand():
    data = readData()
    for entry in data:
        print(json.dumps(entry, indent=2))


def deleteCommand(value):
    data = readData()
    for entry in data:
        if entry['Firstname'].lower() == value.lower() or entry['Lastname'].lower() == value.lower():
            data.remove(entry)
            writeData(data)
            fname = entry['Firstname']
            lname = entry['Lastname']
            print(f"{fname} {lname} deleted. ")
            return


programisrunning = True
while programisrunning:
    userinput=  input('What would you like to do?? \n -a add a person \n -l search \n -d delete a record \n -f search records \n quit')
    userinput = userinput.split()
    if '-a' == userinput[0] and len(userinput) == 5:
        fname, lname, phone, email = userinput[1:]
        addCommand(fname, lname, phone, email)
    elif '-l' == userinput[0] and len(userinput) == 1:
        listCommand()
    elif '-f' == userinput[0] and len(userinput) == 2:
        value = userinput[1]
        findCommand(value)
    elif '-d' == userinput[0] and len(userinput) == 2:
        value = userinput[1]
        deleteCommand(value)
    elif userinput[0] == '-q':
        programisrunning = False


    else:
        print('the proper usage is -f with a first name you dummy. ')
        print('-l lists all recocords. ')
        print('-a firstname and phone email: adds new record. ')
        print('-d with a first name: deletes one record. ')


#addCommand("Leroy", "Bromsey", "899-8809", "leroysmexy@sexystud.com")