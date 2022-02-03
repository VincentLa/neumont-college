import sys

def showUsage():
    print(
    """Please use the following commands: 
        -a Value {adds the value to the datagbase
        -l {shows the content of the database""")

# command line args 
# print(sys.argv)

APPEND_ARG = '-a'
LIST_ARG = '-l'
FILE_NAME = 'data.txt'

args = sys.argv
args_lower = [item.lower() for item in args]

append_value_id = args_lower.count(APPEND_ARG)
list_id = args_lower.count(LIST_ARG)

try:
    
    append_value = args[append_value_id + 1]
    if append_value_id:    
        if len(args_lower) > append_value_id + 1:
            append_value = args[append_value_id + 1]
            
            with  open(FILE_NAME, 'a') as file_handle:  
                file_handle.writelines(append_value +'\n')
            print('Content added')
        else:         
            showUsage()

    if list_id:
        with open(FILE_NAME, 'r') as file_handle:
            print(file_handle.read())
except:
    e = sys.exc_info()[0]
    print(F"""An exception has occured: {e} """)