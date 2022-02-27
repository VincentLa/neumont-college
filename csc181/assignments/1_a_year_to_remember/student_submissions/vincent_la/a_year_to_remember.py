import random

#List of events
events = [
    ('Revolutionary War', 1775),
    ('United States Constitution Signed', 1783),
    ('President Lincoln Assassinated', 1865),
    ("Theodore Roosevelt's first day in office", 1901),
    ('World War II', 1939),
    ('First Personal Computer', 1975),
    ('Berlin Wall Taken Down', 1989),
    ('World War 1', 1914),
    ('Bombing of Japan', 1945),
    ('Ted Bundy Death', 1989)
]

# Function to handle user inputs
def userInput(prompt):

    valid = False
    while not valid:
        try:
            userInput1 = int(input(prompt))
            valid = True
        except:
            print("Input a valid year")
    return userInput1

score = 0
random.shuffle(events)
for i in events:
    print("In what year was %s." %i[0])
    userIn = userInput("Enter in the year: ")
    if userIn == i[1]:
        score += 10
        print('Your guess was correct! \nYour score is %d' %score)
    elif userIn <= i[1] + 5 and userIn >= i[1] - 5:
        score += 5
        print('Your guess was within 5 years from the Date \nYour score is %d' %score)
    elif userIn <= i[1] + 10 and userIn >= i[1] - 10:
        score += 2
        print('Your guess was within 10 years from the Date \nYour score is %d' %score)
    elif userIn <= i[1] + 20 and userIn >= i[1] - 20:
        score += 1
        print('Your guess was within 20 years from the Date \nYour score is %d' %score)
    else:
        print('You were completely off! No points.')

print("Your final score was %d" %score)
