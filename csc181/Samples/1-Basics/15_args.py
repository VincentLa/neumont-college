# Command Arguments

# Python provides a getopt module that helps you parse 
# command-line options and arguments

# The Python sys module provides access to any 
# command-line arguments via the sys.argv. 
# This serves two purposes −
#   sys.argv is the list of command-line arguments.
#   len(sys.argv) is the number of command-line arguments.
# Here sys.argv[0] is the program ie. script name

# Example comsuming commandline arguments
# run this from commandline as 
#       py 15_args.py --help
#       py 15_args.py --l
#       py 15_args.py --a [value]

import sys

print(sys.argv)
args_lower = [item.lower() for item in sys.argv]
print(args_lower)

my_list = ['Scott', 'Dave', 'Lisa']

if '--help' in args_lower:
    print("""
        This is your help system:
        use the following command arguments

        --help (displays this help)
        --l (show list)
        --a (adds value to a list)
    """)
elif '--l' in args_lower:
    print(my_list)
else:
    if args_lower.count('--a'):
        a_index = args_lower.index('--a') 
        a_value = sys.argv[a_index + 1]
        my_list.append(a_value)
        print(my_list)