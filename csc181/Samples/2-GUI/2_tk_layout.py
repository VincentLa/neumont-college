# This is an example of using TK with canvas layouts.
# Tkinter Canvas can be used to draw in a window.
# This will give a nice organization to the window and
# allow you to place controls on the canvases.
# See https://pythonbasics.org/tkinter-canvas/ for more information
import os
import sys
import tkinter
import tkinter.font as tkFont

file_path = os.path.dirname(os.path.realpath(__file__))

root = tkinter.Tk()

# Window Size
root.geometry('600x600')

#=================================
# Functions

def close_window(event):
    sys.exit()

root.bind('<Escape>', close_window)

counter_names = 0

def post_name(key_bind=''):
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
    global entry_name
    counter_names += 1
    listbox_names.insert(counter_names, entry_name.get())
    textbox_names.insert(tkinter.END, entry_name.get() + "\n")
    entry_name.delete(0, 'end')

#=================================
# Layout

# This will create the header that will eventually
# contain the "Welcome to TKinter Demo" text
# See https://www.tutorialspoint.com/python/tk_pack.htm for more
# info on the pack method
canvas_header = tkinter.Canvas(root, height=50)
canvas_header.pack(side='top', fill=tkinter.X)

# This creates a footer which will eventually
# just be green background
canvas_foot = tkinter.Canvas(root, height=50)
canvas_foot.pack(side='bottom', fill=tkinter.X)

# This will create the left side where we 
# will eventually enter in text
canvas_left = tkinter.Canvas(root, width=200)
canvas_left.pack(side='left', fill=tkinter.Y)

# This will create the right side where
# it was eventually contain the ad
canvas_right = tkinter.Canvas(root, width=100)
canvas_right.pack(side='right', fill=tkinter.Y)

# Show the canvas regions
canvas_header.configure(background='red')
canvas_foot.configure(background='green')
canvas_left.configure(background='blue')
canvas_right.configure(background='yellow')

# #=================================

# Font Styles
font_title = tkFont.Font(family='Arial 16 bold', size=20)
font_page = tkFont.Font(family='Arial 16 bold', size=12)

# Controls
label_title = tkinter.Label(canvas_header,
    text='Welcome to the Tkinter Demo',
    font=font_title,
    fg='blue'
    )
label_title.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

lable_name = tkinter.Label(canvas_left,
    text="What is your name?",
    font=font_page,
    fg='blue'
    )
lable_name.grid(column=0, row=0, padx=20)

entry_name = tkinter.Entry(canvas_left)
entry_name.grid(column=0, row=1, pady=5)
entry_name.bind('<Return>', post_name)

button_name = tkinter.Button(canvas_left,
    text='Add name',
    height=1,
    width=10,
    font=font_page,
    command=post_name)
button_name.grid(column=0, row=3, pady=10)

textbox_names = tkinter.Text(canvas_left,
    font=font_page,
    bg='pink',
    height=5,
    width=20)
textbox_names.grid(column=0, row=4, padx=20, pady=10)

# For more info on Listbox: https://www.tutorialspoint.com/python/tk_listbox.htm
# bd = "size of border"
# bg = "Color of background"
listbox_names = tkinter.Listbox(root,
    font=font_page,
    width=25,
    bd=1,
    bg='light blue')
listbox_names.pack(side='left', fill=tkinter.Y)

image_ad = tkinter.PhotoImage(file=os.path.join(file_path, 'ad.gif'))
canvas_right.create_image(0,0,
    anchor='nw',
    image=image_ad)

# Drawing
# Not super material, but notice this creates a blue drawing
# in the bottom right of the canvas.
# Just demonstrates how you can customize
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

# Start the main loop to show the form
# ---------------------------
root.mainloop()