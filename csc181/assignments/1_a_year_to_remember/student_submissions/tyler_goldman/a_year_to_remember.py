import random
from re import S
events = (
    'the start of the Revolutionary War: 1775',
    'the United States Constitution signed: 1783',
    'President Lincoln assassinated: 1865',
    "Theodore Roosevelt's first day in office as President of the United States: 1901",
    'the beginning of World War II: 1939',
    'the first personal computer introduced: 1975',
    'the Berlin Wall taken down: 1989',
    'the twin towers fall: 2001',
    "Barack Obama's first day in office as President: 2009",
    'Covid-19 strikes the world: 2020'
)
eventList = list(events)
print(type(eventList[0]))
random.shuffle(eventList)
Nevents = tuple(eventList)
v1, v2, v3, v4, v5, v6, v7, v8, v9, v10 = Nevents

print(v1[-4:])

def playGame():
    try:
        score = 0
        print('Welcome to A Year To Remember! Where we ask you "important" events in time and you must input the year! On to the first round!')
        answer = input("What Year was " + v1[0:-6] + "? ")
        if answer == v1[-4:]:
            print('WOW! YOU GOT THAT RIGHT ON THE MONEY! YOU GET 10 POINTS!')
            score += 10
        elif (int(answer) <= (int(v1[-4:]) + 5)) and (int(answer) >= (int(v1[-4:]) - 5)):
            print('Hey, you were pretty close! 5 Points! The correct answer was: ' + v1[-4:])
            score += 5
        elif (int(answer) <= (int(v1[-4:]) + 10)) and (int(answer) >= (int(v1[-4:]) - 10)):
            print('Well, you were close enough. 2 points. The correct answer was: ' + v1[-4:])
            score += 2
        elif (int(answer) <= (int(v1[-4:]) + 20)) and (int(answer) >= (int(v1[-4:]) - 20)):
            print('At least you get a point... The correct answer was: ' + v1[-4:])
            score += 1
        else:
            print('are you even trying? you are off by 20 years! no points! The correct answer was: ' + v1[-4:])
            score += 0
        print('Your current score is: ' + str(score))

        answer = input("What Year was " + v2[0:-6] + "? ")
        if answer == v2[-4:]:
            print('WOW! YOU GOT THAT RIGHT ON THE MONEY! YOU GET 10 POINTS!')
            score += 10
        elif (int(answer) <= (int(v2[-4:]) + 5)) and (int(answer) >= (int(v2[-4:]) - 5)):
            print('Hey, you were pretty close! 5 Points! The correct answer was: ' + v2[-4:])
            score += 5
        elif (int(answer) <= (int(v2[-4:]) + 10)) and (int(answer) >= (int(v2[-4:]) - 10)):
            print('Well, you were close enough. 2 points. The correct answer was: ' + v2[-4:])
            score += 2
        elif (int(answer) <= (int(v2[-4:]) + 20)) and (int(answer) >= (int(v2[-4:]) - 20)):
            print('At least you get a point... The correct answer was: ' + v2[-4:])
            score += 1
        else:
            print('are you even trying? you are off by 20 years! no points! The correct answer was: ' + v2[-4:])
            score += 0
        print('Your current score is: ' + str(score))
        
        answer = input("What Year was " + v3[0:-6] + "? ")
        if answer == v3[-4:]:
            print('WOW! YOU GOT THAT RIGHT ON THE MONEY! YOU GET 10 POINTS!')
            score += 10
        elif (int(answer) <= (int(v3[-4:]) + 5)) and (int(answer) >= (int(v3[-4:]) - 5)):
            print('Hey, you were pretty close! 5 Points! The correct answer was: ' + v3[-4:])
            score += 5
        elif (int(answer) <= (int(v3[-4:]) + 10)) and (int(answer) >= (int(v3[-4:]) - 10)):
            print('Well, you were close enough. 2 points. The correct answer was: ' + v3[-4:])
            score += 2
        elif (int(answer) <= (int(v3[-4:]) + 20)) and (int(answer) >= (int(v3[-4:]) - 20)):
            print('At least you get a point... The correct answer was: ' + v3[-4:])
            score += 1
        else:
            print('are you even trying? you are off by 20 years! no points! The correct answer was: ' + v3[-4:])
            score += 0
        print('Your current score is: ' + str(score))
        
        answer = input("What Year was " + v4[0:-6] + "? ")
        if answer == v4[-4:]:
            print('WOW! YOU GOT THAT RIGHT ON THE MONEY! YOU GET 10 POINTS!')
            score += 10
        elif (int(answer) <= (int(v4[-4:]) + 5)) and (int(answer) >= (int(v4[-4:]) - 5)):
            print('Hey, you were pretty close! 5 Points! The correct answer was: ' + v4[-4:])
            score += 5
        elif (int(answer) <= (int(v4[-4:]) + 10)) and (int(answer) >= (int(v4[-4:]) - 10)):
            print('Well, you were close enough. 2 points. The correct answer was: ' + v4[-4:])
            score += 2
        elif (int(answer) <= (int(v4[-4:]) + 20)) and (int(answer) >= (int(v4[-4:]) - 20)):
            print('At least you get a point... The correct answer was: ' + v4[-4:])
            score += 1
        else:
            print('are you even trying? you are off by 20 years! no points! The correct answer was: ' + v4[-4:])
            score += 0
        print('Your current score is: ' + str(score))
        

        answer = input("What Year was " + v5[0:-6] + "? ")
        if answer == v5[-4:]:
            print('WOW! YOU GOT THAT RIGHT ON THE MONEY! YOU GET 10 POINTS!')
            score += 10
        elif (int(answer) <= (int(v5[-4:]) + 5)) and (int(answer) >= (int(v5[-4:]) - 5)):
            print('Hey, you were pretty close! 5 Points! The correct answer was: ' + v5[-4:])
            score += 5
        elif (int(answer) <= (int(v5[-4:]) + 10)) and (int(answer) >= (int(v5[-4:]) - 10)):
            print('Well, you were close enough. 2 points. The correct answer was: ' + v5[-4:])
            score += 2
        elif (int(answer) <= (int(v5[-4:]) + 20)) and (int(answer) >= (int(v5[-4:]) - 20)):
            print('At least you get a point... The correct answer was: ' + v5[-4:])
            score += 1
        else:
            print('are you even trying? you are off by 20 years! no points! The correct answer was: ' + v5[-4:])
            score += 0
        print('Your current score is: ' + str(score))
        

        answer = input("What Year was " + v6[0:-6] + "? ")
        if answer == v6[-4:]:
            print('WOW! YOU GOT THAT RIGHT ON THE MONEY! YOU GET 10 POINTS!')
            score += 10
        elif (int(answer) <= (int(v6[-4:]) + 5)) and (int(answer) >= (int(v6[-4:]) - 5)):
            print('Hey, you were pretty close! 5 Points! The correct answer was: ' + v6[-4:])
            score += 5
        elif (int(answer) <= (int(v6[-4:]) + 10)) and (int(answer) >= (int(v6[-4:]) - 10)):
            print('Well, you were close enough. 2 points. The correct answer was: ' + v6[-4:])
            score += 2
        elif (int(answer) <= (int(v6[-4:]) + 20)) and (int(answer) >= (int(v6[-4:]) - 20)):
            print('At least you get a point... The correct answer was: ' + v6[-4:])
            score += 1
        else:
            print('are you even trying? you are off by 20 years! no points! The correct answer was: ' + v6[-4:])
            score += 0
        print('Your current score is: ' + str(score))
        


        answer = input("What Year was " + v7[0:-6] + "? ")
        if answer == v7[-4:]:
            print('WOW! YOU GOT THAT RIGHT ON THE MONEY! YOU GET 10 POINTS!')
            score += 10
        elif (int(answer) <= (int(v7[-4:]) + 5)) and (int(answer) >= (int(v7[-4:]) - 5)):
            print('Hey, you were pretty close! 5 Points! The correct answer was: ' + v7[-4:])
            score += 5
        elif (int(answer) <= (int(v7[-4:]) + 10)) and (int(answer) >= (int(v7[-4:]) - 10)):
            print('Well, you were close enough. 2 points. The correct answer was: ' + v7[-4:])
            score += 2
        elif (int(answer) <= (int(v7[-4:]) + 20)) and (int(answer) >= (int(v7[-4:]) - 20)):
            print('At least you get a point... The correct answer was: ' + v7[-4:])
            score += 1
        else:
            print('are you even trying? you are off by 20 years! no points! The correct answer was: ' + v7[-4:])
            score += 0
        print('Your current score is: ' + str(score))
        


        answer = input("What Year was " + v8[0:-6] + "? ")
        if answer == v8[-4:]:
            print('WOW! YOU GOT THAT RIGHT ON THE MONEY! YOU GET 10 POINTS!')
            score += 10
        elif (int(answer) <= (int(v8[-4:]) + 5)) and (int(answer) >= (int(v8[-4:]) - 5)):
            print('Hey, you were pretty close! 5 Points! The correct answer was: ' + v8[-4:])
            score += 5
        elif (int(answer) <= (int(v8[-4:]) + 10)) and (int(answer) >= (int(v8[-4:]) - 10)):
            print('Well, you were close enough. 2 points. The correct answer was: ' + v8[-4:])
            score += 2
        elif (int(answer) <= (int(v8[-4:]) + 20)) and (int(answer) >= (int(v8[-4:]) - 20)):
            print('At least you get a point... The correct answer was: ' + v8[-4:])
            score += 1
        else:
            print('are you even trying? you are off by 20 years! no points! The correct answer was: ' + v8[-4:])
            score += 0
        print('Your current score is: ' + str(score))
        

        answer = input("What Year was " + v9[0:-6] + "? ")
        if answer == v9[-4:]:
            print('WOW! YOU GOT THAT RIGHT ON THE MONEY! YOU GET 10 POINTS!')
            score += 10
        elif (int(answer) <= (int(v9[-4:]) + 5)) and (int(answer) >= (int(v9[-4:]) - 5)):
            print('Hey, you were pretty close! 5 Points! The correct answer was: ' + v9[-4:])
            score += 5
        elif (int(answer) <= (int(v9[-4:]) + 10)) and (int(answer) >= (int(v9[-4:]) - 10)):
            print('Well, you were close enough. 2 points. The correct answer was: ' + v9[-4:])
            score += 2
        elif (int(answer) <= (int(v9[-4:]) + 20)) and (int(answer) >= (int(v9[-4:]) - 20)):
            print('At least you get a point... The correct answer was: ' + v9[-4:])
            score += 1
        else:
            print('are you even trying? you are off by 20 years! no points! The correct answer was: ' + v9[-4:])
            score += 0
        print('Your current score is: ' + str(score))
        

        answer = input("What Year was " + v10[0:-6] + "? ")
        if answer == v10[-4:]:
            print('WOW! YOU GOT THAT RIGHT ON THE MONEY! YOU GET 10 POINTS!')
            score += 10
        elif (int(answer) <= (int(v10[-4:]) + 5)) and (int(answer) >= (int(v10[-4:]) - 5)):
            print('Hey, you were pretty close! 5 Points! The correct answer was: ' + v10[-4:])
            score += 5
        elif (int(answer) <= (int(v10[-4:]) + 10)) and (int(answer) >= (int(v10[-4:]) - 10)):
            print('Well, you were close enough. 2 points. The correct answer was: ' + v10[-4:])
            score += 2
        elif (int(answer) <= (int(v10[-4:]) + 20)) and (int(answer) >= (int(v10[-4:]) - 20)):
            print('At least you get a point... The correct answer was: ' + v10[-4:])
            score += 1
        else:
            print('are you even trying? you are off by 20 years! no points! The correct answer was: ' + v10[-4:])
            score += 0
    except:
        print("ay stupido use the number keys only, now you have to restart the quiz! DISQUALIFIED!!!")
    else:
        print("ALRIGHT PENCILS DOWN! THE QUIZ IS OVER!!!!!!!!!!!!!!!!!!!!!!!!! WE ARE NOW TALLYING UP THE SCORE")
        print("calculating...")
        print("calculating...")
        print("calculating...")
        print("calculating...")
        print("calculating...")
        print("calculating...")
        if score == 100:
            print("WOOOOOOOOOOWIE ZOOOOOOOOOOWIE!!!!!!!!! YOU BLASTED IT OUT OF THE PARK! ARE YOU CHEATING? OR IS YOUR BRAIN THAT MASSIVE?! OH WELL YOU WIN THE SATISFACTION OF WINNING 100 POINTS")
        elif score <= 99 and score >= 90:
            print("Nice job! You did Amazing! Your final total was: " + str(score))
        elif score <= 89 and score >= 80:
            print("Wow! You did Very Well! Your final total was: " + str(score))
        elif score <= 79 and score >= 70:
            print("Nice! You did Pretty Good! Your final total was: " + str(score))
        elif score <= 69 and score >= 60:
            print("Well. You did enough. Your final total was: " + str(score))
        elif score <= 59 and score >= 50:
            print("You have a medium brain. Your final total was: " + str(score))
        elif score <= 49 and score >= 40:
            print("You need to get better! Your final total was: " + str(score))
        elif score <= 39 and score >= 30:
            print("Try Harder! Your final total was: " + str(score))
        elif score <= 29 and score >= 20:
            print("You dont have enough brain. Your final total was: " + str(score))
        elif score <= 19 and score >= 10:
            print("Sorry your history knowledge is not up to snuff. Your final total was: " + str(score))
        elif score <= 9 and score >= 1:
            print("Your brain is quite small! Your final total was: " + str(score))
        else:
            print("WHERE IS YOUR BRAIN! HOW DID YOU GET EVERY QUESTION WRONG?! Your final total was: " + str(score))
playGame()
close= input("Please press enter to close the cmd line. And Have a wonderful Morning/Afternoon/Evening/Night! ")