from ast import Compare
import random

list_of_events = [
    ('When did the American Revolution start', 1775),
    ('When was the U.S. Constitution signed', 1783),
    ('When was President Lincoln is assassinated', 1865),
    ("When was President T. Roosevelt's first day in office", 1901),
    ('When did World War 2 Start', 1939),
    ('When did the First Personal Computer release', 1975),
    ('When did The Berlin Wall fall', 1989),
    ('When did Leif Eriksson discovers North America', 1000),
    ('When did the Titanic sinks', 1912),
    ('When did England start sending convicts to Australlia', 1788),
]
questions = random.shuffle(list_of_events)
print(list_of_events)

userscore = 0

userInput = int(input())

#print("Please enter your guess")
#userInput = int(input())

class Logic:
    if (userInput == list_of_events):{
        print("That was correct. you earned 10 points")
        :userscore+10
        }

    elif(userInput == list_of_events+5):{
        print("You were five too high. You earned 5 points")
        :userscore+5
        }

    elif(userInput == list_of_events+10):{
        print("You were 10 too high. You earned 2 points")
        :userscore+2
    }

    elif(userInput == list_of_events+20):{
        print("You were 20 too high. You earned 1 points")
        :userscore+1
    }

    elif(userInput == list_of_events-5):{
        print("You were five too low. You earned 5 points")
        :userscore+5
        }

    elif(userInput == list_of_events-10):{
        print("You were 10 too low. You earned 2 points")
        :userscore+2
    }

    elif(userInput == list_of_events-20):{
        print("You were 20 too low. You earned 1 points")
        :userscore+1
    }

    else:
        print("your score was too high or too low. You earned zero points")
        
while list_of_events < 10:
    print(len(list_of_events))
    userInput
    Logic

    continue
else:
    print("Please input a number")       