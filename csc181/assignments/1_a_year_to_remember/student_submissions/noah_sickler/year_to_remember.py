from ast import Try
import random
points = []

Questions = [
    ("What year did the Revolutionary War begin?", 1775),
    ("When was the United States Constitution signed?", 1787),
    ("When was President Lincoln assassinated?", 1865),
    ("What year was Theodore Roosevelt's sworn in as President?", 1901),
    ("When was the beginning of World War II?", 1939),
    ("In what year was the first personal computer introduced?", 1975),
    ("In what year was the Berlin Wall taken down?", 1989),
    ("When was the United States founded?", 1776),
    ("When was the UN formed?", 1945),
    ("James Garfiled was what number of President of the United States?", 20)
]
random.shuffle(Questions)

print("\n\nWelcome to Year to Remember: Guess that year!")

try:
    for questionInput, a in Questions:

        while True:
            userInput = input("\n{questionInput}: ")
            if userInput.isdigit():
                userInput = int(userInput)
                break
            else:
                print("Only Number values allowed! Please Try Again!")
        difference = abs(userInput - a)

        if userInput == a:
            print("\nEinstein over here!")

            points.append(10)
            print("+10 points!!! CORRECT!")

        elif difference <= 5:
            print("\nNot quite there, Almost!")

            points.append(5)
            print("You got +5 points!")

        elif difference <= 10:
            print("\n10 years away... read more")

            points.append(2)
            print("+2 points, you can do better!")

        elif difference <= 20:
            print("\nWhat? Not even close!")
            
            points.append(1)
            print("Congragulations!! You got 1 point!")

        else:
            print("\nYikes! out of the park with that questionInput")
            points.append(0)

            print("\nTry again for points, +0!\n\n")

    finalScore = sum(points)
    print("Total Points: ", finalScore )

    try:
        quit = userInput("\n\nEnter 'y' to quit.")
        if quit == "y":
            exit()
        else:
            print("Oh well....")
            exit()
    except:
        print('')

except:
    print("Please only enter numbers! Try Again!")