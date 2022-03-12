from tkinter import *
from tkinter import messagebox
import json
import os
import pickle

file_path = os.path.dirname(os.path.realpath(__file__))

def createTask():
    task = enterTask.get()
    if task != "":
        lbTasks.insert(END, task)
        enterTask.delete(0, "end")
    else:
        messagebox.showwarning(title="Warning!", message="Please enter a task.")

def deleteTask():
    lbTasks.delete(ANCHOR)
    
def loadTask():
    try:
        tasks = pickle.load(open("tasks.json", "rb"))
        lbTasks.delete(0, "end")
        for task in tasks:
            lbTasks.insert("end", task)
    except:
        messagebox.showwarning(title="Warning!", message="Cannot find tasks.json")
        
    
def saveTask():
    tasks = lbTasks.get(0, lbTasks.size())
    pickle.dump(tasks, open("tasks.json", "wb"))
    
    
ws = Tk()
ws.geometry('500x450+500+200')
ws.config(bg='#59546C')
ws.resizable(width=False, height=False)
ws.attributes('-fullscreen',True)


module1Label = Label(ws, text="Module 1: ToDo List" , width='20', background='#59546C', font='Verdana 14 bold')
module1Label.place(x=170, y=250)

module2Label = Label(ws, text="Module 2: TBD" , width='20', background='#59546C', font='Verdana 14 bold')
module2Label.place(x=850, y=250)

module3Label = Label(ws, text="Module 3: TBD" , width='20', background='#59546C', font='Verdana 14 bold')
module3Label.place(x=1400, y=250)

#Listbox Frame
frame = Frame(ws)
frame.pack(pady=10)
frame.place(x=120, y=300)

#ListBox
lbTasks = Listbox(
    frame,
    width=30,
    height=12,
    font=('Verdana', 14),
    fg='#2D080A',
    highlightthickness=0,
    selectbackground='#2D080A',
    bd=0,
    activestyle="none",
    
)
lbTasks.pack(side=LEFT, fill=BOTH)
files = [('JSON File', '*.json')]

#Scrollbar
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)
lbTasks.config(xscrollcommand=sb.set)
sb.config(command=lbTasks.yview)

#Enter Task
enterTask = Entry(
    ws,
    font=('Verdana', 20),
    width=20
    
    )

#Enter Task Frame
enterTask.pack(pady=20)
enterTask.place(x=140,y=800)

#Add/Del Task Frame
button_frame1 = Frame(ws)
button_frame1.pack(pady=20)
button_frame1.place(x=200,y=600)

#Add Task Button
addTask_btn = Button(
    button_frame1,
    text='Add',
    font=('Verdana 14'),
    bg='#66b447',
    padx=30,
    pady=10,
    command=createTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

#Delete Task Button
delTask_btn = Button(
    button_frame1,
    text='Delete',
    font=('Verdana 14'),
    bg='#cb4154',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

#Save/Load Task Frame
button_frame2 = Frame(ws)
button_frame2.pack(pady=40)
button_frame2.place(x=200,y=670)

#Save Task Button
saveTask_btn = Button(
    button_frame2,
    text='Save',
    font=('Verdana 14'),
    bg='#2EB0E8',
    padx=26,
    pady=10,
    command=saveTask
)
saveTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

#Load Task Button
loadTask_btn = Button(
    button_frame2,
    text='Load',
    font=('Verdana 14'),
    bg='#E8BE2E',
    padx=26,
    pady=10,
    command=loadTask
)
loadTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

#Exit button
exit_button = Button(ws, text="Exit", command=ws.destroy)
exit_button.pack(pady=20)
exit_button.place(x=1850,y=20)

ws.mainloop()