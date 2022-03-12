#To-Do list
from tkinter import *
import sys
import json
import os


dir_path = os.path.dirname(os.path.realpath(__file__))

json_filename = os.path.join(dir_path, 'todo_list_storage.json')

root = Tk()

root.geometry('1000x800')
root.configure(background='blue')

def newItem():
    global entry_item
    try:
        with open(json_filename, 'r') as file:
            todolist = json.loads(file.read())
            todolist_length = len(todolist)
            todolist.update({todolist_length: entry_item.get()})
        with open(json_filename, 'w') as file:
            file.write(json.dumps(todolist))
    except:
        with open(json_filename,'a') as file:
            file.write(json.dumps({0: entry_item.get()}))
    entry_item.delete(0,'end')
    


def printList():
    global todolist
    global todolist_box
    todolist_box.delete(0, END)
    with open(json_filename,'r') as file:
        todolist = json.loads(file.read())
    for key, value in todolist.items():
        todolist_box.insert(END, value + "\n")

def deleteItem():
    global remove_Item
    
    with open(json_filename, "r") as file:
        currentList = json.loads(file.read())
        del currentList[remove_Item.get()]
    with open(json_filename,'w') as file:
        file.write(json.dumps(currentList))
    


label_title = Label(root,
    text="This is a ToDo list organizer")
label_title.place(anchor='center', relx=.5, rely=.2)

entry_item = Entry(root)
entry_item.place(
    anchor='center',
    relx=.4,
    rely=.3
)
  
button_add_item = Button(
    root,
    text="New Entry",
    width=10,
    command=newItem
)
button_add_item.place(anchor='center', relx=.4, rely=.4)

todolist_box = Listbox(root,
    width=35,
    bd=1,
    bg="green")
todolist_box.place(anchor='center', relx=.5, rely=.6)

button_show_list = Button(
    root,
    text="Show List",
    width=12,
    command=printList
)
button_show_list.place(anchor='center', relx=.5, rely=.4)

remove_Item = Entry(root)
remove_Item.place(
    anchor='center',
    relx=.6,
    rely=.3
)
button_delete_item = Button(root,
    text='Remove Item',
    width=12,
    command=deleteItem
)
button_delete_item.place(anchor='center', relx=.6, rely=.4)

def close_window(event):
    sys.exit()
    
root.bind('<Escape>', close_window) 



#add Music player

#song_name = tkinter.Label(root,
#    text="No song playing right now",
#    )
#song_name.place(
#    anchor='center',
#    relx=.2,
#    rely=.2
#)

#button_start_music = tkinter.Button(root,
#    text="start music",
#    width=10,
#    command=
#    )
#button_start_music.place(anchor='center', relx=.2, rely=.3)


#add stopwatch 

counter=-1
running=False
def stopwatch_label(lbl):
    def count():
        if running:
            global counter
            if counter==-1:
                display="00"
            else:
                display=str(counter)

            lbl['text']=display

            lbl.after(1000, count)
            counter += 1
    count()                
def StartTimer(lbl):
    global running
    running=True
    stopwatch_label(lbl)
    start_button['state']='disabled'
    stop_button['state']='normal'
    reset_button['state']='normal'

def StopTimer():
    global running
    start_button['state']='normal'
    stop_button['state']='disabled'
    reset_button['state']='normal'
    running = False

def ResetTimer(lbl):
    global counter
    counter=-1
    if running==False:      
        reset_button['state']='disabled'
        lbl['text']='00'
    else:                          
        lbl['text']=''

lbl = Label(
    root, text="00"
)
lbl.place(anchor='center', relx=.8, rely=.2)

lable_msg = Label(
    root, text="minutes"
)
lable_msg.place(anchor='center',relx=.9, rely=.2)

start_button= Button(
    root, 
    text='Start', 
    width=15, 
    command=lambda:StartTimer(lbl)
    )
start_button.place(anchor='center', relx=.8, rely=.4)    

stop_button = Button(
    root, 
    text='Stop', 
    width=15, 
    state='disabled', 
    command=StopTimer
    )
stop_button.place(anchor='center', relx=.8, rely=.5)    

reset_button = Button(
    root, 
    text='Reset', 
    width=15, 
    state='disabled', 
    command=lambda:ResetTimer(lbl)
    )
reset_button.place(anchor='center', relx=.8, rely=.6)

root.mainloop()