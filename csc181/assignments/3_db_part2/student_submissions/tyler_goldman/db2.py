
import argparse
import json 
# def add(args):
#     with open('db.json', 'r') as json_file:
#         feeds = json.load(json_file)
#     with open('db.json', 'w') as json_file:
#         entry = {'Firstame': args.name, 'phone': args.phone, 'email': args.email}
#         feeds.append(entry)
#         json.dump(feeds, json_file)

# def read() :
#     with open ('db.json') as file:
#         return json.load(file)
    
parser = argparse.ArgumentParser(description='Files And Text')
parser.add_argument('-a', nargs='+', required = False)
args = parser.parse_args()

if(args.a):
    count=0
    entry="{"
    for _, value in parser.parse_args()._get_kwargs():
        if value is not None:
            if(count == 0):
                entry= entry + "FirstName: " + value[count] + ",\n"
                count+=1
            if(count == 1):
                entry= entry + 'LastName: ' + value[count] + ",\n"
                count+=1
            if(count == 2):
                entry= entry + 'Phone: ' + value[count] + ",\n"
                count+=1
            if(count == 3):
                entry= entry + 'Email: ' + value[count]
                count+=1
        
    entry = entry + '}'
    with open('db.json','r+') as file:
        file_data = json.load(file)
        file_data["Details"].append(entry)
        file.seek(0)
        json.dump(file_data, file, indent = 4)   
        file.close()
# elif(args.l):
#     l = args.l
#     print(read())

