import random

quiz_questions = [("the start of the Revolutionary War ", 1775),
                  ("the United States Constitution signed", 1783),
                  ("President Lincoln assassinated", 1865),
                  ("Theodore Roosevelt's first day in office as President of the United States", 1901),
                  ("the beginning of World War II", 1939),
                  ("the first personal computer introduced", 1975),
                  ("the Berlin Wall taken down", 1989),
                  ("the beginning of the civil rights movement", 1954),
                  ("the end of the great depression", 1933),
                  ("alcohol banned in the US", 1920)]
random.shuffle(quiz_questions)
score = 0
play_again = True
while play_again:
    user_dumb = True
    for question in quiz_questions:
        while user_dumb:
            try:
                user_dumb = False
                print(f"What year was {question[0]}?")
                guess = int(input())
            except:
                user_dumb = True
                print("The input must be a number")
        if guess == question[1]:
            score += 10
            print("you are exactly right! 10 points!")
        elif question[1] + 5 >= guess >= question[1] - 5:
            score += 5
            print("you were very close! Off by at most 5 years! 5 points!")
        elif question[1] + 10 >= guess >= question[1] - 10:
            score += 2
            print("well within the ball park, you're within 10 years of the event. 2 points.")
        elif question[1] + 20 >= guess >= question[1] - 20:
            score += 1
            print("you have the right idea, but you're only within 20 years. 1 point.")
        else:
            print("You weren't close enough, no points...")
        print("correct year: " + str(question[1]))
        print("your current score is: " + str(score))
        user_dumb = True

    print(f"your final score is {score} points!")

    while user_dumb:
        print("Play again? (Y)es or (N)o")
        answer = input().upper()
        if answer == 'Y' or answer == 'N':
            user_dumb = False
            if answer == 'Y':
                play_again = True
            else:
                play_again = False
        else:
            print("The input must be Y or N")
