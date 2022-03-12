import sys
import tkinter
import time 
import random

questions = [
    ("the start of the Revolutionary War", 1775),
    ("the United Constitution signed", 1783),
    ("President Lincoln assassinated", 1865),
    ("Theodore Roosevelt's first day in office as President of the United States", 1901),
    ("the beginning of World War II", 1939),
    ("the first personal computer introduced", 1975),
    ("the Berlin Wall taken down ", 1989),
    ("Neumont founded", 2003),
    ("the first episode of Scooby-Doo aired", 1969),
    ("Skyrim's first release (Not the Special or Legendary Editions)", 2011)
]

questionLead = "What Year was "

root = tkinter.Tk()

root.geometry('600x400')
root.config(background='blue')

gameDisplay = tkinter.Label(root, text='Click Start Game to Begin')
gameDisplay.place(anchor='center', relx=.5, rely=.1)

gameEntry = tkinter.Entry(root)
gameEntry.place(anchor='center', relx=.3, rely=.5)

gameLabel = tkinter.Label(root, text='Click Start Game')
gameLabel.place(anchor='center', relx=.7, rely=.5)

gameButton = tkinter.Button(root, text='Start Game')
gameButton.place(anchor='center', relx=.5, rely=.5)


guess = tkinter.IntVar()



def getValidData():
    global guess
    global gameLabel
    global gameEntry
    try:
        UG = int(gameEntry.get())
        assert UG > 0
        guess.set(UG)
    except:
        gameLabel.config(text='Please Enter a 4 digit Year (use leading Zeros if you need to)')
    finally:
        gameEntry.delete(0, 'end')

def runGame():
    global guess
    global gameDisplay
    global gameButton
    global gameLabel
    gameEntry.delete(0, 'end')
    gameButton.config(text='Guess Year', command=getValidData)
    userPoints = 0
    random.shuffle(questions)
    for quest in questions:
        gameLabel.config(text='Your Points: ' + str(userPoints))
        gameDisplay.config(text=questionLead+quest[0])
        guess = tkinter.IntVar()

        gameButton.wait_variable(guess)
        guess = guess.get()

        if guess == quest[1]:
            
            userPoints += 10
        elif quest[1]-5 < guess < quest[1]+5:
            
            userPoints += 5
        elif quest[1]-10 < guess < quest[1]+10:
            
            userPoints += 2
        elif quest[1]-20 < guess < quest[1]+20:

            userPoints += 1
        else:
            print('hello')
            
            gameDisplay.config(text='Not Close at all, No Points for You')
            gameDisplay.update()
            time.sleep(1.75)
        gameLabel.config(text='Correct Answer: ' + str(quest[1]))
        gameLabel.update()
        time.sleep(1.75)
        counter = 0

    gameButton.config(text="Start New Game", command=runGame)
    finalScore = "You Earned "+ str(userPoints) + " Points!!!"
    if userPoints == 100:
        gameDisplay.config(text="Congratulations!!! You got all of them right!!!" + finalScore)
    elif userPoints > 90:
        gameDisplay.config(text="That is pretty good you really know you years" + finalScore)
    elif userPoints > 50:
        gameDisplay.config(text="Acceptable, you pass" + finalScore)
    elif userPoints >= 10:
        gameDisplay.config(text="Might need to work on you chronology" + finalScore)
    else:
        gameDisplay.config(text="You didn't get even one right or even close" + finalScore)

gameButton.config(command=runGame)

def close_window(event):
    sys.exit()

root.bind('<Escape>', close_window)

root.mainloop()