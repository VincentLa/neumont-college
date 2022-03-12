import datetime
import time
import tkinter
# import winsound
import json
from threading import *
from tkinter.ttk import *
from time import strftime
from datetime import datetime, timezone
from tkinter import *


root = Tk()
root.title('Clock')
counter = 66600
running = False

root.geometry("400x200")
  
def Threading():
    t1= Thread(target=alarm)
    t1.start()
  
def alarm():
    
    while True:
       
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
  
        
        time.sleep(1)
  
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
  
        if current_time == set_alarm_time:
            print("Wakey Wakey")
            # winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
  
Label(root,text="Alarm Clock",font=("Times 20 bold"),fg="pink").pack(pady=10)
Label(root,text="Set Time",font=("Times 15 bold")).pack()


def write_json(new_data, filename='data.json'):
    with open(filename,'r') as file:
        
        file_data = json.load(file)
        
        file_data.update(new_data)
        
        file.seek(0)
        
        json.dump(file_data, file, indent = 4)
        
    
frame = Frame(root)
frame.pack()
  
hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0])
  
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)
  
minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')

minute.set(minutes[0])
  
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)
  
second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])
  
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)
  
Button(root,text="Set Your Alarm",font=("Times 15"),command=Threading).pack(pady=20)

def counter_label(label):
    def count():
        if running:
            global counter
   
            if counter==66600:            
                display="Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display=string
   
            label['text']=display   
   
            label.after(1000, count) 
            counter += 1
   
    count()     
   
def Start(label):
    global running
    running=True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
   
def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False

def Reset(label):
    global counter
    counter=66600
   
    if running==False:      
        reset['state']='disabled'
        label['text']='Welcome!'
   
    else:               
        label['text']='Starting...'
   
root = tkinter.Tk()
root.title("Stopwatch")
   
root.minsize(width=250, height=70)
label = tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
label.pack()
f = tkinter.Frame(root)
start = tkinter.Button(f, text='Start', width=6, command=lambda:Start(label))
stop = tkinter.Button(f, text='Stop',width=6,state='disabled', command=Stop)
reset = tkinter.Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label))
f.pack(anchor = 'center',pady=5)
start.pack(side="left")
stop.pack(side ="left")
reset.pack(side="left")

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)
 
# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'purple',
            foreground = 'white')
 
# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor = 'center')
time()
 

  
root.mainloop()
