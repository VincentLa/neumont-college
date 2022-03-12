from logging import NullHandler
from tkinter import *
from tkinter import messagebox
from turtle import right
import random


#Establish Tinker window
tinkerWindow = Tk()
tinkerWindow.geometry('500x450+500+200')
tinkerWindow.title('To-Do List v2')
tinkerWindow.config(bg='#000000')

taskBoxFrame = Frame(tinkerWindow)
taskBoxFrame.pack(pady=10)

taskBox = Listbox(
    taskBoxFrame,
    width=40,
    height=12,
    font=('Poppins', 11)
)
taskBox.pack(side=BOTTOM, fill=BOTH)

#Added a scroll bar so you can scroll through your tasks
scrollBar = Scrollbar(taskBoxFrame)
scrollBar.pack(side=RIGHT, fill = BOTH)

taskBox.config(yscrollcommand = scrollBar.set)
scrollBar.config(command = taskBox.yview)
#--------------------------------------------------------

listMotive = [
    ('"You miss 100 percent of the shots you dont take" - Wayne G.'),
    ('“We cannot solve problems with the kind of thinking we employed when we came up with them.” — Albert Einstein'),
    ('“Either you run the day or the day runs you.” - Jim Rohn'),
    ('“Setting goals is the first step in turning the invisible into the visible.” - Tony Robbins'),
    ('“It’s not about better time management. It’s about better life management” - Alexandra of The Productivity Zone'),
    ('"Do it now, you gotta do it later anyways" - Noah Sickler')
]

dummy_list = [
    'Tasks show up here',
    'click on me, then delete :)',
    ]
for item in dummy_list:
        taskBox.insert(END, item)


userInput = Entry(
    tinkerWindow,
    font=('Poppins', 18)
    )
userInput.pack(side=TOP, pady=20 )

def addTask():
    task = userInput.get()
    if task != "":
        taskBox.insert(END, task)
        userInput.delete(0, "end")
    else:
        #added call to give a warning if they hit enter without text
        messagebox.showwarning("!!! WARNING !!!", "Enter something before you add")
        
def deleteTask():
    taskBox.delete(ANCHOR)

def motivate():
    headsUp = messagebox.showinfo('Motivation Station', random.choice(listMotive))
    #Impossible to change how big messagebox is 
    return headsUp


buttonFrame = Frame(tinkerWindow)
buttonFrame.pack(pady=20)

addButton = Button(
    buttonFrame,
    text='Add Task',
    font=('Poppins', 14),
    bg='#c5f776',
    padx=20,
    pady=10,
    command = addTask
)
addButton.pack(fill=BOTH, expand=True, side=LEFT)

deleteButtom = Button(
    buttonFrame,
    text='Delete Task',
    font=('Poppins', 14),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command = deleteTask
)
deleteButtom.pack(fill=BOTH, expand=True, side=RIGHT)

#added color to the buttons to looks nicer
motivateButtom = Button(
    buttonFrame,
    text='Click for Motitavtion',
    font=('Poppins', 14),
    bg='#FFE933',

    command = motivate
)
motivateButtom.pack(fill=BOTH, expand=True, side=BOTTOM)
 
tinkerWindow.mainloop()