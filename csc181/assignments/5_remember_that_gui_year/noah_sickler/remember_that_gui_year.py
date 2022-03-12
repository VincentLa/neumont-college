from os import system
import random
from tkinter import *
from tkinter import messagebox

root = Tk()

tuple1=("the start of the Revolutionary War",1775)
tuple2=("the United States Constitution signed",1783)
tuple3=("President Lincoln assassinated",1865)
tuple4=("Theodore Roosevelt's first day in office as President of the United States",1901)
tuple5=("the beginning of World War II",1939)
tuple6=("the first personal computer introduced",1975)
tuple7=("the Berlin Wall taken down",1989)
tuple8=("First mobile phone call ever made",1973)
tuple9=("the begining of Vietnam war",1955)
tuple10=("Moon landing",1969)


questionList = [tuple1,tuple2,tuple3,tuple4,tuple5,tuple6,tuple7,tuple8,tuple9,tuple10]
random.shuffle(questionList)

global count 
count = 0

global question
global answer
question = questionList[count]
answer = question[-1]

def onClick():
        
    userInput = e.get() 
    global userPoints
    global count
    count =+ 1
   
    if int(userInput) == question[-1]:
        userPoints = 10 
        output = "Correct!! ++" + str(userPoints) + " Points"
        resLabel = Label(root, text=output)
        resLabel.pack()
        e.delete(0, 'end')

    elif question[-1]+5 < int(userInput) or int(userInput) > question[-1]-5:
        userPoints = 5 
        output = "Close! Within 5 tho! ++"  + str(userPoints) + " Points"
        resLabel = Label(root, text=output)
        resLabel.pack()
        e.delete(0, 'end')

    elif question[-1]+10 < int(userInput) or int(userInput) > question[-1]-10:
        userPoints = 2
        output = "Within 10 years!! ++" + str(userPoints) + " Points"
        resLabel = Label(root, text=output)
        resLabel.pack()
        e.delete(0, 'end')

    elif question[-1]+20 < int(userInput) or int(userInput) > question[-1]-20:
        userPoints = 1
        output = "ooo maybe look at the books. ++" + str(userPoints) + " Points"
        resLabel = Label(root,text= output)
        resLabel.pack()
        e.delete(0, 'end')

def popup():
    question = questionList[count]
    output = "What year was " + question[0] + "? \n"
    messagebox.showinfo("Quesiton", output)

quesButton = Button(root, text ="Receive Question", command=popup)
quesButton.pack()

e = Entry(root, width= 20, borderwidth=3)
e.pack()
   
subButton = Button(root, text="Submit",command=onClick)
subButton.pack()

def close_window(event):
    system.exit()
    root.bind('<Escape>', close_window)

def checkS():
    Label(root,text=str(userPoints))
    Label.pack()

checkscore = Button(root, text="Current Score: ",command=checkS)
checkscore.pack()
    
root.mainloop()