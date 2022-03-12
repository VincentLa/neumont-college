from logging import NullHandler
from tkinter import *
from turtle import right



#Establish Tinker window
tinkerWindow = Tk()
tinkerWindow.geometry('500x450+500+200')
tinkerWindow.title('To-Do List')
tinkerWindow.config(bg='#000000')
#userFont = tkFont.Font(family="Helvetica",size=36,weight="bold")

taskBoxFrame = Frame(tinkerWindow)
taskBoxFrame.pack(pady=10)

taskBox = Listbox(
    taskBoxFrame,
    width=40,
    height=12,
    font=('Poppins', 11)
)
taskBox.pack(side=BOTTOM, fill=BOTH)

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
#userInput.pack(pady=20, side=BOTTOM, Fill=Both)
#Find out why 'side' isnt working

#add a Task to UI
def addTask():
    task = userInput.get()
    if task != "":
        taskBox.insert(END, task)
        userInput.delete(0, "end")
    else:
        NullHandler
        
#Remove a task form GUI
def deleteTask():
    taskBox.delete(ANCHOR)

buttonFrame = Frame(tinkerWindow)
buttonFrame.pack(pady=20)

#Clickable button to add and delete
addButton = Button(
    buttonFrame,
    text='Add Task',
    font=('Poppins', 14),
    padx=20,
    pady=10,
    command = addTask
)
#Need, Dont delete will remove button
addButton.pack(fill=BOTH, expand=True, side=LEFT)

#Delete Button
deleteButtom = Button(
    buttonFrame,
    text='Delete Task',
    font=('Poppins', 14),
    padx=20,
    pady=10,
    command = deleteTask
)
deleteButtom.pack(fill=BOTH, expand=True, side=RIGHT)

#Helps the program run 
tinkerWindow.mainloop()