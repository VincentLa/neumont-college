# GUI using TKinter

# You can specify each object required from tkinter or import everyting
# ---------------------------
#from tkinter import Tk, Label, Entry

from tkinter import *
import sys      # Import sys to close

# Initialize a Tk form
# ---------------------------
root = Tk()

# Control the window 
# ---------------------------
root.geometry('600x400')                        # Window Size
#root.configure(background='red')               # Window background
#root.attributes('-alpha', 0.5)                 # Window transparancy
#root.wm_attributes('-transparentcolor', 'red') # Window transparent color

# Labels
# ---------------------------
label_title = Label(root,
    text='Welcome to my Tkinter Demo')
label_title.grid(column=1, row=1)

label_title2 = Label(root,
    text='This is another line')
label_title2.grid(column=1, row=0)

label_title3 = Label(root,
    text='Place this label')
label_title3.place(anchor='center', relx=.5, rely=.1)

# Entry
# ---------------------------
entry_name = Entry(root)
entry_name.place(anchor='center', 
    relx=.5, 
    rely=.2)

# Button
# ---------------------------
def print_name():
    print(entry_name.get())
    label_title3.config(text=entry_name.get())

button_show_name = Button(root, 
    text='Print name',
    width=10,
    command=print_name)
button_show_name.place(anchor='center', relx=.5, rely=.3)

# Bind window to key strokes
# ---------------------------
def close_window(event):
    sys.exit()

root.bind('<Escape>', close_window) # Call close_window when hit escape 

# Start the mail loop to show the form
# ---------------------------
root.mainloop()