from tkinter import *

import tkinter.font as tkfont
import sys
import random

root = Tk()


root.geometry("600x400")
canvas_header = Canvas(root, height= 50)
canvas_header.pack(side= 'top', fill=X)
canvas_footer = Canvas(root, height=50)
canvas_footer.pack(side="bottom", fill=BOTH)
font_title = tkfont.Font(family="Arial 16 bold", size=20)

Label_title = Label(canvas_header, text = "A Year To Remember", font = font_title, fg='blue')
Label_title.place(relx = 0.5, rely= .5, anchor=CENTER)



points = []

Year = [
    ("What year did the Revoultionary war start?", 1775),
    ("When was the United States Constitution signed?", 1783),
    ("When was President Lincoln assassinated?", 1865),
    ("What year was Theodore Roosevelt's first day in office as president?", (1901)),
    ("When was the beginning of World War II?", (1939)),
    ("In what year was the first personal computer introduced?", (1975)),
    ("In what year was the Berlin Wall taken down?", (1989)),
    ("When was the first submarine used?", 1776),
    ("Which year did Texas become a state? ", 1845),
    ("Which year the U.S. Stock Market faced the Black Monday? ", 1987)
]


question_count = 0 
user_input = 100
score = 0 

#list of tupils - pass in a single element but is also returning the answer
random.shuffle(Year)
that_Random = Year.copy()
print(that_Random)



    
def button_press():
    global question_count, user_input, Year, score
    print("question:", Year[question_count][0])
    difference = abs(Year[question_count][1] - user_input)
    if Year[question_count][1] == user_input:
        score += 10
    elif difference > 5:
        pass
    elif difference > 10:
        pass
    else: 
        score += 1
    question_count += 1
    #gotta fix this 
    # if button == button_press:
    #     return that_Random
     
    
    

entry = Entry(root)
button = Button(root, text='Submit', command=button_press)
label = Label(root, text="{}".format(that_Random[0]))
Current_Score = Label(root, text=f"Score: {score}")

label.pack()
entry.pack()
button.pack()
Current_Score.pack()

def close_window(event):
    sys.exit()
root.bind('<Escape>', close_window)

root.mainloop()