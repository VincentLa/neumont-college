import argparse

py = argparse.ArgumentParser(description="This is a database text file")
py.add_argument('-a', type=str, required=False, help="text to add to file")
py.add_argument('-l', action='store_true', required=False, help="Use this switch to list file contents")

args = py.parse_args()

a = args.a
l = args.l



try:  
    data = open('data.txt', "w")
    data.write("Database created")
    data.close()
    print('File created')

    if(l == True):
        data = open('data.txt', 'r')
        info = data.read()
        data.close
        print(info)

except:
    print("There is no file named data")  
   
with open('data.txt','a') as file:
    file.write(a)