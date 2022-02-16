import random

questions = [('the start of the Revolutionary War', '1775'), 
             ('the United States Constitution signed','1783'),
             ('President Lincoln assassinated','1865'),
             ("Theodore Roosevelt's first day in office as President of the United States", '1901'),
             ('the beginning of World War II', '1939'),
             ('the first personal computer introduced', '1975'),
             ('the Berlin Wall taken down','1989'),
             ('the day christopher columbus discovered america', '1492'),
             ('President JFK assassinated','1963' ),
             ('Covid originally started', '2019' )]

random.shuffle(questions)
print(questions[0])

score = 0
iteration = 0
x = 0
try:
    while iteration < 10:
        answer = input('What year was ' + str(questions[x]))
        if answer == int(questions[x]):
            print('Congrats! you were dead on! 10 points for you' )
            score = score + 10;
        elif answer == range(int(questions[x]), int(questions[x]) + 5):
            print('You were within 5 years! 5 points for you')
            score = score + 5;
        elif answer == range(int(questions[x]) - 5, int(questions[x])):
            print('You were within 5 years! 5 points for you')
            score = score + 5;
        elif answer == range(int(questions[x]), int(questions[x])) + 10:
            print('You were within 10 years! 2 points for you')
            score = score + 2;
        elif answer == range(int(questions[x]) - 10, int(questions[x])):
            print('You were within 10 years! 2 points for you')
            score = score + 2;
        elif answer == range(int(questions[x]), int(questions[x]) + 20):
            print('You were within 20 years! 1 point for you')
            score = score + 1;
        elif answer == range(int(questions[x]) - 20, int(questions[x])):
            print('You were within 20 years! 1 point for you')
            score = score + 1;
        else:
            print('you were waaaaaaaaaay off, better luck next time')
        iteration = iteration + 1
        x = x + 1
    if score == 100:
        print('Congrats! Perfect score of ' + score + " points")
    elif score > 90:
        print('You were pretty good! you got ' + score + " points")
    elif score > 70:
        print('You were alright. You got ' + score + " points")
    elif score > 50:
        print('You did decent. You got ' + score + " points")
    elif score > 30:
        print('You did pretty bad not gonna lie. You got ' + score + " points")
    elif score < 31:
        print('You need to brush up on your history. You got ' + score + " points")
except: 
    print('Please enter a valid integar')