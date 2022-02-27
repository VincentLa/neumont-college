import argparse
import json

def loadData():
    data = list()
    try:
        file = open("db.json", "r")
        data = json.loads(file.read())
        file.close()
    except:
        pass
    return data

def saveData(data):
    with open("db.json", "w") as file:
        file.write(json.dumps(list(data), indent=4))

def printEntry(entry):
    print("Name: " + str(entry["fname"]) + " " + str(entry["lname"]))
    print("Phone #: " + str(entry["phone"]))
    print("Email Address: " + str(entry["email"]))

def findEntry(searchString, data):
    for idx, x in enumerate(data):
        if str(x["fname"]).lower() == str(searchString).lower() or str(x["lname"]).lower() == str(searchString).lower():
            return idx
    return -1


parser = argparse.ArgumentParser(description="Database CLI Controller")
parser.add_argument("-a", default="", type=str, required=False, help="Adds a record to the database using the following format: -a \"[fname] [lname] [phone] [email]\"")
parser.add_argument("-l", action="store_true", required=False, help="Lists all the stored records")
parser.add_argument("-f", default="", type=str, required=False, help="Finds a specific record by searching the first or last name")
parser.add_argument("-d", default="", type=str, required=False, help="Finds and Deletes a record")

args = parser.parse_args()

a = args.a 
l = args.l
f = args.f 
d = args.d 

if(len(a) > 0):
    newRecord = str(a).split(" ")
    if len(newRecord) == 4:
        data = list(loadData())
        data.append({
            "fname" : newRecord[0],
            "lname" : newRecord[1],
            "phone" : newRecord[2],
            "email" : newRecord[3]
        })

        print(f"{newRecord[0]} {newRecord[1]} has been added to the data")
        saveData(data)
    else:
        print("If you wish enter a new record, than please enter the inforamation in the following format:")
        print("-a \"[fname] [lname] [phone] [email]\"")

elif l:
    data = loadData()
    print("-" * 50)
    for x in data:
        printEntry(x)
        print("-" * 50)
elif(len(f) > 0):
    data = loadData()
    entryIndex = findEntry(str(f), list(data))
    if(entryIndex == -1):
        print("There isn't any one with that name in the record")
        print("If you entered a full name, try entering only a first name or a last name")
    else:
        printEntry(data[entryIndex])
elif(len(d) > 0):
    data = loadData()
    entryIndex = findEntry(str(d), list(data))
    if(entryIndex == -1):
        print("There isn't any one with that name in the record to delete")
        print("If you entered a full name, try entering only a first name or a last name")
    else:
        print(f"{data[entryIndex]['fname']} {data[entryIndex]['lname']} has been deleted from the record")
        del data[entryIndex]
        saveData(data)
else:
    print('db -a "fname lname phone email": adds new record\ndb -l: lists all records\ndb -f search: finds one record\ndb -d search: deletes one record')