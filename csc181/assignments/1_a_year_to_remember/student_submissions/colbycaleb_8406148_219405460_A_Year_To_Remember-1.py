import random


questions = [
    ("the start of the Revolutionary War", 1775),
    ("the United Constitution signed", 1783),
    ("President Lincoln assassinated", 1865),
    ("Theodore Roosevelt's first day in office as President of the United States", 1901),
    ("the beginning of World War II", 1939),
    ("the first personal computer introduced", 1975),
    ("the Berlin Wall taken down ", 1989),
    ("Neumont founded", 2003),
    ("the first episode of Scooby-Doo aired", 1969),
    ("Skyrim's first release (Not the Special or Legendary Editions)", 2011)
]

questionLead = "What Year was "

random.shuffle(questions)

userPoints = 0

for x in questions:
    print("\n\nPlease enter the year in which you othink the event occured")
    completeQuestion = questionLead + x[0] + "?"
    try:
        userGuess = int(input(completeQuestion))
        assert userGuess >= 0
        if userGuess == x[1]:
            print("That is correct. 10 points for you")
            userPoints += 10
        elif x[1]-5 < userGuess < x[1]+5:
            print("Close but not quite. 5 points for you")
            userPoints += 5
        elif x[1]-10 < userGuess < x[1]+10:
            print("Not Exactly but not bad. 2 points for you")
            userPoints += 2
        elif x[1]-20 < userGuess < x[1]+20:
            print("Could be better but you are at least still in the ballpark. Only 1 point")
            userPoints += 1
        else:
            print("Not close at all, No points at all")
    except:
        print("Please enter a 4-digit year. \nNo points will be awarded for this question")
    
    print("You have " + str(userPoints) + " points so far")


print("\n\n\n\nYou Earned "+ str(userPoints) + " Points!!!")
if userPoints == 100:
    print("Congratulations!!! You got all of them right!!!")
elif userPoints > 90:
    print("That is pretty good you really know you years")
elif userPoints > 50:
    print("Acceptable, you pass")
elif userPoints >= 10:
    print("Might need to work on you chronology")
else:
    print("You didn't get even one right or even close")
