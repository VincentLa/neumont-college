import os
from tkinter import Tk, Label, Frame, Button, Entry, Canvas, PhotoImage

file_path = os.path.dirname(os.path.realpath(__file__))

root = Tk()
root.title('Tkinter Demo')

counter=0
def countUp():
    global counter
    counter +=1
    label_counter.config(text=str(counter))

def countDown():
    global counter
    counter -=1
    label_counter.config(text=str(counter))

def doEntry():
    label_title.config(text="Hello " + entry_name.get() + "!")

# https://www.tutorialspoint.com/python/tk_label.htm
# fg = "Color of text"
label_title = Label(
    text="Tkinter Demo",
    fg="#007", # This is a hex color, see https://www.color-hex.com/color-palette/5915
    font="Arial 20 bold italic"
)
label_title.grid(column=1, row=0)

frame_counter = Frame(root)
frame_counter.grid(column=2, row=1)

label_counter = Label(frame_counter,
    text="0",
    justify='center',
    bg='#fab',
    fg='black',
    relief='groove',
    width=4,
    font='Arial 16 bold' 
)
label_counter.pack(side='top')

btn_counter_up = Button(frame_counter,
    text='Up',
    bg='#004',
    fg='#ff0',
    width=9,
    command=countUp
)
btn_counter_up.pack(side='top')

btn_counter_down = Button(frame_counter,
    text='Down',
    bg='#004',
    fg='#ff0',
    width=9,
    command=countDown
)
btn_counter_down.pack(side='top')

frame_entry = Frame(root)
frame_entry.grid(column=0, row=1)

Label(
    frame_entry,
    text='Name: '
).pack(side='top')

entry_name = Entry(frame_entry)
entry_name.pack(side='top')

btn_entry = Button(frame_entry,
    text='Submit',
    width=9,
    command=doEntry
)
btn_entry.pack(side='top')

canvas = Canvas(root,
    width=200,
    height=300,
    bg='#000'
)
canvas.grid(column=1, row=1)

img_wasp = PhotoImage(file=os.path.join(file_path, 'wasp.gif'))
wasp_y = 0

def animloop():
    global wasp_y
    canvas.delete('all')

    

    canvas.create_image(0, wasp_y, anchor='nw', image=img_wasp)

    wasp_y += 1

    if wasp_y > 300:
        wasp_y = -120

    canvas.create_text(100,150,
        text='Howdy!',
        font='Verdana 14 bold',
        fill='#ff0'
    )

    for i in range(0, 200, 10):
        canvas.create_line(200, 100+i, 200-i, 300, fill='#0b0')

    canvas.create_rectangle(20, 50, 40, 70, fill='#f00')
    canvas.after(10, animloop)


animloop()

# Start the main loop to show the form
# ---------------------------
root.mainloop()