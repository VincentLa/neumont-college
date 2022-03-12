import tkinter
import tkinter.font as tkFont
import random
import sys
from turtle import right

list_of_events = [
    ('When did the American Revolution start', 1775),
    ('When was the U.S. Constitution signed', 1783),
    ('When was President Lincoln is assassinated', 1865),
    ("When was President T. Roosevelt's first day in office", 1901),
    ('When did World War 2 Start', 1939),
    ('When did the First Personal Computer release', 1975),
    ('When did The Berlin Wall fall', 1989),
    ('When did Leif Eriksson discovers North America', 1000),
    ('When did the Titanic sinks', 1912),
    ('When did England start sending convicts to Australlia', 1788),
]
questions = random.shuffle(list_of_events)

#while 
current_question = 0

while current_question<len(list_of_events):
    outputQuestion = list_of_events[current_question]
    current_question = current_question+1

root = tkinter.Tk()


root.geometry('800x600')                        
root.configure(background='dark blue')

canvas_right = tkinter.Canvas(root, width=100)
canvas_right.pack(side='right', fill=tkinter.Y)

label_title3 = tkinter.Label(root,
    text= outputQuestion)

label_title3.place(anchor='center', relx=.5, rely=.2)

def close_window(event):
    sys.exit()

root.bind('<Escape>', close_window)

counter_names = 0

def post_geuss(key_bind=''):
    """
    Function for posting the name to canvas

    Keyword Args:
        key_bind: Eventually we will bind a key e.g. <Return>
        so that if the user hits "Return" it will also post the
        name to canvas
    """
    global counter_names
    global listbox_names
    global testbox_names
    global entry_geuss
    counter_names += 1

    textbox_names.insert(tkinter.END, entry_geuss.get() + "\n")

    entry_geuss.delete(0, 'end')

entry_geuss = tkinter.Entry(root)
entry_geuss.place(
    anchor='center', 
    relx=.5, 
    rely=.3
)
entry_geuss.bind('<Return>', post_geuss)

button_show_geuss = tkinter.Button(
    root, 
    text='Entry Geuss',
    width=10,
    command=post_geuss
)
button_show_geuss.place(anchor='center', relx=.5, rely=.4)

canvas_left = tkinter.Canvas(root, width=200)
canvas_left.pack(side='left', fill=tkinter.Y)  

listbox_names = tkinter.Listbox(canvas_right,
    width=20,
    bd=1,
    bg="green")
listbox_names.pack(side='right',fill=tkinter.Y)    

textbox_names = tkinter.Text(canvas_left,
    bg='pink',
    height=5,
    width=20)
textbox_names.grid(column=0, row=4, padx=20, pady=10)


root.mainloop()