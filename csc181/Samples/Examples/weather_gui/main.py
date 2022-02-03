from tkinter import messagebox
from tkinter import *
import weather_form

def main():
    root = Tk()
    root.title('My Toolbox')
    root.geometry("300x200")

    # Sample function
    def say_hi():
        messagebox.showinfo('Title', "Hi ya'll")

    menu_bar = Menu(root)

    # Tools menu #1 as dropdown (cascade)
    menu_1 = Menu(menu_bar, tearoff=0)
    menu_1.add_command(label='Say hi!', command=say_hi)
    menu_1.add_command(label='Weather Update', command=weather_form.weather_update)

    # Add menus to the menu_bar
    menu_bar.add_cascade(label='Tools', menu=menu_1)
    menu_bar.add_command(label='Quit', command=root.quit)

    root.config(menu=menu_bar)

    title_var = StringVar()
    main_title = Label(root, textvariable=title_var)
    title_var.set('Welcome to my Toolbox')
    main_title.pack()

    root.mainloop()

if __name__ == '__main__':
    main()
    