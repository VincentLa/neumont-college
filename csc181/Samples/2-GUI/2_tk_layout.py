# This is an example of using TK with canvas layouts
# this will give a nice organization to the window and
# allow you to place controls on the canvases/

from tkinter import *
import tkinter.font as tkFont
import sys

root = Tk()

# Window Size
root.geometry('600x600')

#=================================
# Functions

def close_window(event):
    sys.exit()

root.bind('<Escape>', close_window)

counter_names = 0

def post_name(arg=''):
    global counter_names
    counter_names += 1
    listbox_names.insert(counter_names, entry_name.get())
    textbox_names.insert(END, entry_name.get() + "\n")
    entry_name.delete(0, 'end')

#=================================
# Layout
canvas_header = Canvas(root, height=50)
canvas_header.pack(side='top', fill=X)

canvas_foot = Canvas(root, height=50)
canvas_foot.pack(side='bottom', fill=BOTH)

canvas_left = Canvas(root, width=200)
canvas_left.pack(side='left', fill=BOTH)

canvas_right = Canvas(root, width=100)
canvas_right.pack(side='right', fill=BOTH)

# Show the canvas regions
canvas_header.configure(background='red')
canvas_foot.configure(background='green')
canvas_left.configure(background='blue')
canvas_right.configure(background='yellow')

#=================================

# Font Styles
font_title = tkFont.Font(family='Arial 16 bold', size=20)
font_page = tkFont.Font(family='Arial 16 bold', size=12)

# Controls
label_title = Label(canvas_header,
    text='Welcome to the Tkinter Demo',
    font=font_title,
    fg='blue'
    )
label_title.place(relx=0.5, rely=0.5, anchor=CENTER)

lable_name = Label(canvas_left,
    text="What is your name?",
    font=font_page,
    fg='blue'
    )
lable_name.grid(column=0, row=0, padx=20)

entry_name = Entry(canvas_left)
entry_name.grid(column=0, row=1, pady=5)
entry_name.bind('<Return>', post_name)

button_name = Button(canvas_left,
    text='Add name',
    height=1,
    width=10,
    font=font_page,
    command=post_name)
button_name.grid(column=0, row=3, pady=10)

textbox_names = Text(canvas_left,
    font=font_page,
    bg='pink',
    height=5,
    width=20)
textbox_names.grid(column=0, row=4, padx=20, pady=10)

listbox_names = Listbox(root,
    font=font_page,
    width=25,
    bd=1,
    bg='light blue')
listbox_names.pack(side='left', fill=Y)

image_ad = PhotoImage(file='./2-GUI/ad.gif')
canvas_right.create_image(0,0,
    anchor='nw',
    image=image_ad)

# Drawing
root.update()
for i in range(0, 200, 10):
    canvas_right.create_line(
        # canvas_right.winfo_width(),
        0, 
        int(canvas_right.winfo_height()-200)+i, 
        i, 
        canvas_right.winfo_height(), 
        fill='blue'
    )

root.mainloop()