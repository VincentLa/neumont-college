import tkinter as tk
from tkinter import *
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
question_number = 0
score = 0
quiz_guess = ""

root = Tk()
root.resizable(False, False)
root.geometry("600x200")
root.title("Remember That Gui Year")
guess_var = tk.StringVar()


question = tk.Label(root, text=f"What year was {quiz_questions[question_number][0]}?").place(x=50,y=125,width=500)
score_display = tk.Label(root, text=f"Score: {score}").place(x=50,y=150,width=100)
guess = Entry(root)
    # .place(x=250,y=150,width=100)
guess.pack()
guess.place(y=25,x=250,width=100)

def guesser():
    global score
    global question_number
    try:
        quiz_guess = int(guess.get())
    except:
        help = tk.Label(root, text="The input must be a number.").place(x=50,y=75,width=500)
        return
    if quiz_guess == quiz_questions[question_number][1]:
        score += 10
        help = tk.Label(root, text="you are exactly right! 10 points!").place(x=50,y=75,width=500)
    elif quiz_questions[question_number][1] + 5 >= quiz_guess >= quiz_questions[question_number][1] - 5:
        score += 5
        help = tk.Label(root, text="you were very close! Off by at most 5 years! 5 points!").place(x=50,y=75,width=500)
    elif quiz_questions[question_number][1] + 10 >= quiz_guess >= quiz_questions[question_number][1] - 10:
        score += 2
        help = tk.Label(root, text="well within the ball park, you're within 10 years of the event. 2 points.").place(x=50,y=75,width=500)
    elif quiz_questions[question_number][1] + 20 >= quiz_guess >= quiz_questions[question_number][1] - 20:
        score += 1
        help = tk.Label(root, text="you have the right idea, but you're only within 20 years. 1 point.").place(x=50,y=75,width=500)
    else:
        help = tk.Label(root, text="You weren't close enough, no points...").place(x=50,y=75,width=500)
    score_display = tk.Label(root, text=f"Score: {score}").place(x=50,y=150,width=100)
    question_number += 1
    question = tk.Label(root, text=f"What year was {quiz_questions[question_number][0]}?").place(x=50,y=125,width=500)
    guess.delete(0,END)


guess_button = tk.Button(root,text="Submit Guess", command=guesser).place(x=400,y=20,width=100,height=50)

root.mainloop()