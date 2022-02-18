import argparse

parser = argparse.ArgumentParser(description='Put your description here')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-a', default="", type=str, help='text to add to a file')
group.add_argument('-l', action='store_true', help='Use this switch to list file contents')

args = parser.parse_args()

a = args.a 
l = args.l

if len(a) > 0:
    with open("data.txt", "a") as file:
        file.write(a + "\n")
elif l == True:
    try:
        content = ""
        with open("data.txt", "r") as file:
            content = file.read()
        print(content)
    except(FileNotFoundError):
        print("The File has not been created yet and cannot therefore not be read")
