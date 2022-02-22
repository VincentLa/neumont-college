import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', type=str,required=False)
parser.add_argument('-l', action='store_true')
args = parser.parse_args()

a = args.a
l = args.l

if l:
    try:
        file1 = open("data.txt","r")
        print(file1.read())
        file1.close()
    except:
        print("File does not exist yet. Store data using the -a command.")
else:
    file1 = open("data.txt","a")
    file1.write(a+"\n")
    file1.close()