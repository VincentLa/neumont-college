import argparse
import json
import os
import string

class Record:
    def __init__(self, fname, lname, phone, email):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email
    
    def tojson(self):
        if os.path.exists("data.json"):
            with open('data.json', 'a') as file:
                file.write(",")
        data='{{"fname":"{0}","lname":"{1}","phone":"{2}","email":"{3}"}}'.format(self.fname,self.lname,self.phone,self.email)
        print("{0} {1} added".format(self.fname,self.lname))
        data_json = json.loads(data)
        # print(data_json)
        # print(json.dumps(data_json))
        with open('data.json', 'a') as file:
            file.write(json.dumps(data_json))

parser = argparse.ArgumentParser(description="text:")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-a", type=str, required=False, help='"fname lname phone email": adds new record')
group.add_argument("-l", action="store_true", required=False, help="lists all records")
group.add_argument("-f", type=str, required=False, help="finds one record")
group.add_argument("-d", type=str, required=False, help="deletes one record")
group.add_argument("-q", action="store_true", required=False, help="quits")

args = parser.parse_args()

a = args.a
l = args.l
f = args.f
d = args.d
q = args.q
if a!=None:
    # if os.path.exists("data.txt"):
    #     print("content added")
    # else:
    #     print("new file created, content added")
    data = a.split()
    if len(data)!=4:
        print('"fname lname phone email"')
    else:
        record=Record(data[0],data[1],data[2],data[3])
        record.tojson()
elif l:
    try:
        with open('data.json', 'r') as file:
            all_data = json.loads("["+file.read()+"]")
        print(all_data)
    except:
        print("File does not exist yet")
elif f!=None:
    try:
        with open('data.json', 'r') as file:
            all_data = json.loads("["+file.read()+"]")
            for data in all_data:
                f=f.lower()
                if data["fname"]==f or data["lname"]==f:
                    print(data)
                    break
    except:
        print("File does not exist yet")
elif d!=None:
    try:
        removed=False
        data_json=""
        with open('data.json', 'r') as file:
            all_data = json.loads("["+file.read()+"]")
            for data in all_data:
                d=d.lower()
                if data["fname"]==d or data["lname"]==d:
                    print("{0} {1} has been removed".format(data["fname"],data["lname"]))
                    all_data.remove(data)
                    data_json=all_data
                    removed=True
                    break
        if removed:
            with open('data.json', 'w') as file:
                file.write(json.dumps(data_json).replace("[","").replace("]",""))
    except:
        print("File does not exist yet")
elif q:
    print("you have exited")
else:
    print("input not right")