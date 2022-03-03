import tkinter
import tkinter.font as tkFont
import sys
import random
import time

    # TODO
    # Create a file called "remember_that_gui_year.py"

    # Build the GUI so it has a message (like a label but can
    # have multiple lines), an entry, a button, and a second label

    # Use the message to display each question and also respond
    # with feedback telling the correct answer and how close or far
    # the guess was. Also use this message to say when the game is over and the final score.

    # Use the entry to allow the user to enter the year they think
    # is correct. Clear the contents of this after each guess using entry.delete(0, 'end')

    # Use the button to submit the guess

    # Use the second label to display the current score
#==========================================================================
# Building the tkinter application

root = tkinter.Tk()

root.geometry('600x600')

def close_window(event):
    sys.exit()

root.bind('<Escape>', close_window)

font_page = tkFont.Font(family='Arial 16 bold', size=12)


#=========================================================================
# Gobal Variables

count = 0
score = 0
quit = False
userInput1 = tkinter.IntVar()
messagerString = tkinter.StringVar()

# List of events
events = [
    ('Revolutionary War', 1775),
    ('United States Constitution Signed', 1783),
    ('President Lincoln Assassinated', 1865),
    ("Theodore Roosevelt's first day in office", 1901),
    ('World War II', 1939),
    ('First Personal Computer', 1975),
    ('Berlin Wall Taken Down', 1989),
    ('World War 1', 1914),
    ('Bombing of Japan', 1945),
    ('Ted Bundy Death', 1989)
]

random.shuffle(events)


#=============================================================================
# Tkinter functions

def userIn():
    try:
        global userInput1
        global messagerString
        global year_entry
        userInput1.set(int(year_entry.get()))
        year_entry.delete(0,'end')
        messagerString.set("")
    except:
        messagerString.set(messagerString.get() + "\nEntered in incorrect Integer.")



#=============================================================================
# Canvas Options

# canvas_header = tkinter.Canvas(root, height=50)
# canvas_header.pack(side='top', fill=tkinter.X)
#
# canvas_left = tkinter.Canvas(root, width=200)
# canvas_left.pack(side='left', fill=tkinter.Y)
#
# canvas_right = tkinter.Canvas(root, width=200)
# canvas_right.pack(side='right', fill=tkinter.Y)


#=============================================================================
# Setting up the widgets

messageLabel = tkinter.Label(root,
    textvariable=messagerString,
    font = font_page)
messageLabel.place(relx=.5, rely=.4, anchor=tkinter.CENTER)

year_entry = tkinter.Entry(root)
year_entry.place(relx=.5, rely=.45, anchor=tkinter.CENTER)

submitButton = tkinter.Button(root,
    text="submit",
    font=font_page,
    command=userIn)

submitButton.place(relx=.5,rely=.5,anchor=tkinter.CENTER)

secondLabel = tkinter.Label(root,
    text='0',
    font=font_page)
secondLabel.place(relx=.5,rely=.55, anchor=tkinter.CENTER)

while quit == False:
    random.shuffle(events)
    for i in events:
        messagerString.set("In what year was {}?".format(i[0]))
        submitButton.wait_variable(userInput1)
        if userInput1.get() == i[1]:
            score += 10
            messagerString.set("Correct!")
            messageLabel.update()
            time.sleep(1.75)
        elif userInput1.get() <= i[1] + 5 and userInput1.get() >= i[1] - 5:
            score += 5
            messagerString.set("Your guess was within 5 years from the correct date of {}".format(i[1]))
            messageLabel.update()
            time.sleep(1.75)
        elif userInput1.get() <= i[1] + 10 and userInput1.get() >= i[1] - 10:
            score += 2
            messagerString.set("Your guess was within 10 years from the correct date of {}".format(i[1]))
            messageLabel.update()
            time.sleep(1.75)
        elif userInput1.get() <= i[1] + 20 and userInput1.get() >= i[1] - 20:
            score += 1
            messagerString.set("Your guess was within 20 years from the correct date of {}".format(i[1]))
            messageLabel.update()
            time.sleep(1.75)
        else:
            messagerString.set("Your guess was greater than 20 years from the correct date of {}".format(i[1]))
            messageLabel.update()
            time.sleep(1.75)
        secondLabel.config(text=score)
        count += 1
        if count == len(events):
            messagerString.set("Game Over\nFinal score of {}".format(score))
            secondLabel.config(text='')
            root.update()
            quit = True


#=============================================================================
# Running the main loop

root.mainloop()
