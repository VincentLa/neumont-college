from os import system
import sys

# Functions
def clearScreen():
    system('cls')

def separator():
    print('-' * 50)

def help():
    print("""
You may use the following commands at any time:
    help  display this help
    list  list the contents of the file
    add   add a value to the file
    del   deletes the file contents  
    quit  quits the CLI
    """)
    separator()

def add(value):
    file = open('list.txt', 'a')
    file.write(f"{value}\n")
    file.close()

def delete():
    file = open('list.txt', 'w')    
    file.close()

def read():
    file = open('list.txt', 'r')    
    contents = file.read()
    file.close()
    return contents

# Main CLI
clearScreen()
print('Welcome to my CLI')
separator()

looping = True
while looping:
    try:
        value = input('>>> ')
        lower_value = value.lower()

        if lower_value == 'help':
            help()
        elif lower_value == 'quit':
            looping = False
        elif lower_value[:4] == 'add ':            
            add(value[4:])
            print(f"   {value[4:]} was added")
        elif lower_value[:3] == 'del':
            delete()
            print("The contents have been deleted")
        elif lower_value[:4] == 'list':
            separator()
            print('The contents of the list are:')
            print(read())
            separator()
        else:
            print('I do not recognize that command :(')
    except:
        # General exceptions
        e = sys.exc_info()[0]
        print(f"Error: {e}")
    
separator()
print('the CLI has ended')