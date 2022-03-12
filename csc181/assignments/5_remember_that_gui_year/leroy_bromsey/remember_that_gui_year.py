import random
from tkinter import *
from tkinter import messagebox

root = Tk()

tuple1=("the start of the Revolutionary War",1775)
tuple2=("the United States Constitution signed",1783)
tuple3=("was President Lincoln assassinated",1865)
tuple4=("it that Theodore Roosevelt's first day in office as President of the United States",1901)
tuple5=("the beginning of World War II",1939)
tuple6=("the first personal computer introduced",1975)
tuple7=("the Berlin Wall taken down",1989)
tuple8=("First mobile phone call ever made",1973)
tuple9=("the Moon landing",1969)
tuple10=("the begining of Vietnam war",1955)

questionlist = [tuple1,tuple2,tuple3,tuple4,tuple5,tuple6,tuple7,tuple8,tuple9,tuple10]
random.shuffle(questionlist)


global count 
count = 0

global q
global ques
global answer
q = questionlist[count]
ques = q[0]
answer = q[-1]

def myClick():

        
    x = e.get() 
    global tpoint
    global count
    count =+ 1
   
    if int(x) == q[-1]:
        tpoint = 10 
        output = "Spot On! You got " + str(tpoint) + " Points"
        resLabel = Label(root, text=output)
        resLabel.pack()
        e.delete(0, 'end')

    elif q[-1]+5 < int(x) or int(x) > q[-1]-5:
        tpoint = 5 
        output = "It's within 5 years! You got "  + str(tpoint) + " Points"
        resLabel = Label(root, text=output)
        resLabel.pack()
        e.delete(0, 'end')

    elif q[-1]+10 < int(x) or int(x) > q[-1]-10:
        tpoint = 2
        output = "It's within 10 years! You got " + str(tpoint) + " Points"
        resLabel = Label(root, text=output)
        resLabel.pack()
        e.delete(0, 'end')

    elif q[-1]+20 < int(x) or int(x) > q[-1]-20:
        tpoint = 1
        output = "It's within 20 years! You got " + str(tpoint) + " Points"
        resLabel = Label(root,text= output)
        resLabel.pack()
        e.delete(0, 'end')

def popup():
    q = questionlist[count]
    output = "What year was " + q[0] + "?"
    messagebox.showinfo("Quesiton", output)

quesButton = Button(root, text ="check Quesiton", command=popup)
quesButton.pack()

e = Entry(root, width= 20, borderwidth=3)
e.pack()
   
subButton = Button(root, text="Submit",command=myClick)
subButton.pack()

def checkS():
    Label(root,text=str(tpoint))
    Label.pack()

checkscore = Button(root, text="Current Score",command=checkS)
checkscore.pack()

def close_window(event):
    Tk.exit()
root.bind('<Escape>', close_window)
    
root.mainloop()

