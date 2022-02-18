import sys

print(sys.argv)
args_lower = [item.lower() for item in sys.argv]

def add(value):
    with open('data.txt', 'a') as file:
        file.write(value + "\n")

def read():
    with open('data.txt', 'r') as file:
        return file.read()

try:
    if '--help' in args_lower:
        print("""
        Help Menu
        ---------
        You may use the following commands
        ----------------------------------
        --help (Displays the commands you can use)
        --a (After you type --a, you may add whatever you want to the list)
        --l (Shows you the contents within your file)
        """)
    elif '--l' in args_lower:
        print("Your file contents are: ")
        print(read())
    elif '--a' in args_lower:
        a_index = args_lower.index('--a')
        a_value = str(sys.argv[a_index + 1:])
        add(a_value)
        print(f'Value was added')
    else:
        print("""You didn't enter a valid command. Please use one of the following commands:
        --------------------
        Help Menu
        ---------
        You may use the following commands
        ----------------------------------
        --help (Displays the commands you can use)
        --a (After you type --a, you may add whatever you want to the list)
        --l (Shows you the content within your file)
        """)
except:
    print("Sorry, that didnt work.")