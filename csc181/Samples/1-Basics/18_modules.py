# Modules

# Module are like code libraries, a file containing 
# a set of functions you want to include in your application

# Create a module by saving the file with the .py extension

# Import the zz_sub_module
import zz_sub_module 
zz_sub_module.greeting('Scott')

# Import the zz_sub_module but us an alias
import zz_sub_module as mod
print(mod.person_john['age'])

# Import a specific object from zz_sub_module
from  zz_sub_module import person_john
print(person_john['name'])

# Import everything from the zz_sub_module so you don't have 
# to reference the module name or alias

# Note, while this is technically legal python code
# it is not advisable to do this according to PEP 8
# https://www.python.org/dev/peps/pep-0008/#imports
# The reason why is that this makes readability much more
# difficult because you don't know where the function is coming from.
from zz_sub_module import *
greeting('Dave')

