from logging import root
import tkinter as tk
from tkinter import filedialog, Text
from tkinter import *
from tkinter import messagebox
import json
import os
import pickle

file_path = os.path.dirname(os.path.realpath(__file__))

#-----------------------------------------------------------------------------------
#TodoList
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
    
root = Tk()
root.geometry('500x450+500+200')
root.config(bg='#59546C')
root.resizable(width=False, height=False)
root.attributes('-fullscreen',True)


module1Label = Label(root, text="Module 1: ToDo List" , width='20', background='#59546C', font='Verdana 14 bold')
module1Label.place(x=170, y=250)

module2Label = Label(root, text="Module 2: App Auto Executor" , width='30', background='#59546C', font='Verdana 14 bold')
module2Label.place(x=785, y=250)

module3Label = Label(root, text="Module 3: Value Converter" , width='30', background='#59546C', font='Verdana 14 bold')
module3Label.place(x=1350, y=250)

#Listbox Frame
frame = Frame(root)
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
    activestyle="none" 
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
    root,
    font=('Verdana', 20),
    width=20
    )

#Enter Task Frame
enterTask.pack(pady=20)
enterTask.place(x=140,y=800)

#Add/Del Task Frame
button_frame1 = Frame(root)
button_frame1.pack(pady=20)
button_frame1.place(x=200,y=600)

#Add Task Button
addTaskBtn = Button(
    button_frame1,
    text='Add',
    font=('Verdana 14'),
    bg='#66b447',
    padx=30,
    pady=10,
    command=createTask
)
addTaskBtn.pack(fill=BOTH, expand=True, side=LEFT)

#Delete Task Button
delTaskBtn = Button(
    button_frame1,
    text='Delete',
    font=('Verdana 14'),
    bg='#cb4154',
    padx=20,
    pady=10,
    command=deleteTask
)
delTaskBtn.pack(fill=BOTH, expand=True, side=LEFT)

#Save/Load Task Frame
button_frame2 = Frame(root)
button_frame2.pack(pady=40)
button_frame2.place(x=200,y=670)

#Save Task Button
saveTaskBtn = Button(
    button_frame2,
    text='Save',
    font=('Verdana 14'),
    bg='#2EB0E8',
    padx=26,
    pady=10,
    command=saveTask
)
saveTaskBtn.pack(fill=BOTH, expand=True, side=LEFT)

#Load Task Button
loadTaskBtn = Button(
    button_frame2,
    text='Load',
    font=('Verdana 14'),
    bg='#E8BE2E',
    padx=26,
    pady=10,
    command=loadTask
)
loadTaskBtn.pack(fill=BOTH, expand=True, side=LEFT)

#Exit button
exitBtn = Button(root, text="Exit", command=root.destroy)
exitBtn.pack(pady=20)
exitBtn.place(x=1850,y=20)
#End of Todo List
#-----------------------------------------------------------------------------------


#Value Converter

def convertValue():
    num = enterValue.get()
    number=int(num)
    answer=[]
    while(number>0):
        p=number%2
        answer.append(p)
        number=number/2
    answer.reverse()
    lbBinaryValue.insert(str(answer))

#Decimal Label
decimalLabel = Label(root, text="Decimal" , width='20', background='#59546C', font='Verdana 14 bold')
decimalLabel.place(x=1250, y=300)

#Binary Label
binaryLabel = Label(root, text="Binary" , width='20', background='#59546C', font='Verdana 14 bold')
binaryLabel.place(x=1250, y=460)

#Value Listbox Frame
valueframe = Frame(root)
valueframe.pack(pady=10)
valueframe.place(x=1450, y=450)

#Value ListBox
lbBinaryValue = Listbox(
    valueframe,
    width=20,
    height=3,
    font=('Verdana', 14),
    fg='#2D080A',
    highlightthickness=0,
    selectbackground='#2D080A',
    bd=0,
    activestyle="none" 
)
lbBinaryValue.pack(side=LEFT, fill=BOTH)

#Enter Value
enterValue = Entry(
    root,
    font=('Verdana', 20),
    width=15
    )

#Enter Task Frame
enterValue.pack(pady=20)
enterValue.place(x=1450,y=300)

#Convert Button
convertBtn = Button(
    text='Convert',
    font=('Verdana 14'),
    bg='#66b447',
    padx=30,
    pady=10,
    command=convertValue
)

convertBtn.place(x=1500, y=350)


# End of Converter
#-----------------------------------------------------------------------------------


#Application Opener
appList = []
applistframe = Frame(root)

if os.path.isfile('apps.txt'):
    with open('apps.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def addApp():
    for widget in appframe.winfo_children():
        widget.destroy()
    
    filename= filedialog.askopenfilename(initialdir="/", title="Select File",
        filetypes=(("executables","*.exe"), ("all files", "*.*")))
    appList.append(filename)
    print(filename)
    
    for app in appList:
        appLabel = Label(appframe, text=app, bg="white")
        appLabel.pack()
        
def runApps():
    for app in appList:
        os.startfile(app)

appCanvas = Canvas(root, height=400, width=400, bg ="#F3EFE1")
appCanvas.pack()
appCanvas.place(x=775, y=300)

appframe = Frame(root)
appframe.pack()
appframe.place(x=800, y=320)

#Load File/Run Apps Frame
button_frame3 = Frame(root)
button_frame3.pack(pady=40)
button_frame3.place(x=825, y=720)

#Open Apps Button
openFileBtn= Button(
    button_frame3,
    text='Open File',
    font=('Verdana 14'),
    bg='#B4D4E6',
    padx=26,
    pady=10,
    command=addApp
)
openFileBtn.pack(fill=BOTH, expand=True, side=LEFT)

#Run Apps Button
runAppsBtn = Button(
    button_frame3,
    text='Run Apps',
    font=('Verdana 14'),
    bg='#B4D4E6',
    padx=26,
    pady=10,
    command=runApps
)
runAppsBtn.pack(fill=BOTH, expand=True, side=LEFT)


# for app in apps:
#     label = Label(appframe, text=app)
#     label.pack()

root.mainloop()

with open('apps.txt', 'w') as f:
    for app in appList:
        f.write(app + ',')
        
#End of Application Opener
#-----------------------------------------------------------------------------------
