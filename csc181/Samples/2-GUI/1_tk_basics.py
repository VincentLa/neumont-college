# GUI using TKinter

# You can specify each object required from tkinter or import everyting
# ---------------------------
# from tkinter import Tk, Label, Entry
# See https://docs.python.org/3/library/tkinter.html for more information
# Note, Tk is a free and open source cross-platform widget toolkit
# For our use case, it's a good intro to building GUIs in Python
# without other dependencies.
# See https://en.wikipedia.org/wiki/Tk_(software) for more info

import tkinter
import sys      # Import sys to close

# Initialize a Tk form
# Just running this should open a new window
# ---------------------------
root = tkinter.Tk()

# Control the window 
# ---------------------------
root.geometry('600x400')                        # Window Size
root.configure(background='red')                # Window background
# root.attributes('-alpha', 0.5)                  # Window transparancy

# Labels
# ---------------------------
label_title = tkinter.Label(root,
    text='Welcome to my Tkinter Demo')
label_title.grid(column=1, row=1)

label_title2 = tkinter.Label(root,
    text='This is another line')
label_title2.grid(column=1, row=0)

# Anchors specify where the text is positioned relative to the
# reference point (relx, rely)
# See https://www.tutorialspoint.com/python/tk_anchors.htm
# for more information about anchors
label_title3 = tkinter.Label(root,
    text='Place this label')
label_title3.place(anchor='center', relx=.5, rely=.1)
label_title3.config(text='Hello')
label_title3.config(text='bye')

# Entry
# ---------------------------
entry_name = tkinter.Entry(root)
entry_name.place(
    anchor='center', 
    relx=.5, 
    rely=.2
)

# Button
# ---------------------------
def print_name():
    print(entry_name.get())
    label_title3.config(text=entry_name.get())

button_show_name = tkinter.Button(
    root, 
    text='Print name',
    width=10,
    command=print_name
)
button_show_name.place(anchor='center', relx=.5, rely=.3)

# Bind window to key strokes
# ---------------------------
def close_window(event):
    sys.exit()

root.bind('<Escape>', close_window) # Call close_window when hit escape 

# Start the main loop to show the form
# ---------------------------
root.mainloop()