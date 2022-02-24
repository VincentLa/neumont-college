import argparse
import json

py = argparse.ArgumentParser(description="This is a database text file")
recordManage = py.add_mutually_exclusive_group(required=True)

# -a should be append
recordManage.add_argument('-a', type=str, required=False, help="text to add to file")
#-l should be list
recordManage.add_argument('-l', action='store_true', required=False, help="Use this switch to list file contents")
#-f should find and print a record
recordManage.add_argument('-f', type=str)
#-d should find and delete a record
recordManage.add_argument("-d", type=str)



args = py.parse_args()

a = args.a
l = args.l
f = args.f
d = args.d

try:

    if(a ==True):  
        data = open('data.json', "w")
        data.write("Database created")
        with open('data.json','a') as file:
            file.write(json.dumps(a))
        data.close()
        print('File created')

    if(l == True):
        data = open('data.json', 'r')
        info = data.read()
        data.close()
        print(info)

    if(f == True):
        data = open('data.json', "r")
        info = data.read(f)
        data.close()
        print(info)

    if(d == True):
        data = open('data.json', 'd')
        info = data.read(d)
        if data[d] == d:
            data.pop(d)
            
        
except:
    print("There is no file named data")  
   
