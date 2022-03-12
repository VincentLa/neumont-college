import os

from datetime import datetime
import datetime
import tkinter as tk
import json
# global root
from functools import partial
from time import strptime

dir_path = os.path.dirname(os.path.realpath(__file__))

root = tk.Tk()
root.resizable(True, True)
root.geometry("600x700")
root.title("Finally, You May Choose")
global frame
frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)
frame.pack()

task_name = tk.Label(frame, text="Task Name")
task_name.grid(row=0, column=0, padx=10, pady=10)

task_details = tk.Label(frame, text="Task Details")
task_details.grid(row=0, column=1, padx=10, pady=10)

task_time = tk.Label(frame, text="Task Time")
task_time.grid(row=0, column=2, padx=10, pady=10)

global enter_task_name
enter_task_name = tk.Entry(frame)
enter_task_name.grid(row=1,column=0,padx=10,pady=10)

global enter_task_details
enter_task_details = tk.Entry(frame)
enter_task_details.grid(row=1,column=1,padx=10,pady=10)

global enter_task_time
enter_task_time = tk.Entry(frame)
enter_task_time.grid(row=1,column=2,padx=10,pady=10)


def delete_task(deleteIndex):
    with open(os.path.join(dir_path, 'task_data.json')) as json_file:
        data = json.load(json_file)
    if type(data) is str:
        data = json.loads(data)
    data['tasks'].pop(deleteIndex)
    with open(os.path.join(dir_path, 'task_data.json'), 'w') as outfile:
        json.dump(data, outfile)
    # print(data['tasks'])
    reset_frame()
    build_frame(data['tasks'])

def add_task():
    global frame
    global enter_task_time
    global enter_task_name
    global enter_task_details
    with open(os.path.join(dir_path, 'task_data.json')) as json_file:
        data = json.load(json_file)
        # print(type(data))
    if type(data) is str:
        data = json.loads(data)
    add_data = [{'name': enter_task_name.get(),
         'details': enter_task_details.get(),
         'time': enter_task_time.get()}]
    # print(type(data))
    # print(type(add_data))

    data['tasks'] = data['tasks'] + add_data

    reset_frame()
    json_string = json.dumps(data)
    with open(os.path.join(dir_path, 'task_data.json'), 'w') as outfile:
        json.dump(json_string, outfile)

    with open(os.path.join(dir_path, 'task_data.json')) as json_file:
        data = json.load(json_file)
        # print(json.loads(data)['tasks'])
    data = json.loads(data)
    build_frame(data['tasks'])
def build_frame(tasks):
    for x in range(0, len(tasks), 1):
        display_task_name = tk.Label(frame, text=tasks[x]['name'])
        display_task_name.grid(row=x+2, column=0, padx=10, pady=10)

        display_task_details = tk.Label(frame, text=tasks[x]['details'])
        display_task_details.grid(row=x+2, column=1, padx=10, pady=10)

        display_task_time = tk.Label(frame, text=tasks[x]['time'])
        display_task_time.grid(row=x+2, column=2, padx=10, pady=10)

        delete_task_button = tk.Button(frame, text="Delete Task", command=partial(delete_task, x))
        delete_task_button.grid(row=x+2, column=3, padx=10, pady=10)


def reset_frame():
    global frame
    global enter_task_time
    global enter_task_name
    global enter_task_details
    frame.destroy()
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, padx=10, pady=10)
    frame.pack()
    add_task_button = tk.Button(frame, text="Add Task", command=add_task)
    add_task_button.grid(row=0, column=3, padx=10, pady=10)
    task_name = tk.Label(frame, text="Task Name")
    task_name.grid(row=0, column=0, padx=10, pady=10)
    task_details = tk.Label(frame, text="Task Details")
    task_details.grid(row=0, column=1, padx=10, pady=10)
    task_time = tk.Label(frame, text="Task Time")
    task_time.grid(row=0, column=2, padx=10, pady=10)
    enter_task_name = tk.Entry(frame)
    enter_task_name.grid(row=1, column=0, padx=10, pady=10)
    enter_task_details = tk.Entry(frame)
    enter_task_details.grid(row=1, column=1, padx=10, pady=10)
    enter_task_time = tk.Entry(frame)
    enter_task_time.grid(row=1, column=2, padx=10, pady=10)


# def organize():

add_task_button = tk.Button(frame,text="Add Task", command=add_task)
add_task_button.grid(row=0,column=3,padx=10,pady=10)

with open(os.path.join(dir_path, 'task_data.json')) as json_file:
    data = json.load(json_file)
    # print(type(data))
    if type(data) is str:
        data = json.loads(data)
    build_frame(data['tasks'])
root.mainloop()
