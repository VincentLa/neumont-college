# Input and try/except
num1 = input()
print(num1)

try:
    print("Welcome to the add program")
    n1 = int(input("Enter the first number: "))
    n2 = input("Enter the second number: ")

    print(f"The added numbers are: {n1 + int(n2)}")

except:
    print("Please only enter numbers")


# Using assert to check a condition. If the assert condition fails, the program will error
assert 1 == 5

######
# Importing from library
######
import random

mylist = ['apple', 'banana', 'cherry']
random.shuffle(mylist)
print(mylist)