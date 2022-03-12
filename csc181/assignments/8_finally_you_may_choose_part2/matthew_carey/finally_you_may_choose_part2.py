import smtplib
import ssl
from datetime import datetime
import datetime
import glob
import os.path
import tkinter as tk
import json
from functools import partial
from time import strptime

root = tk.Tk()
root.resizable(True, True)
root.geometry("1400x700")
root.title("Finally, You May Choose")
global frame
global file_directory
global list_of_task_files
global current_task_file
current_task_file = "Tutorialtask_data.json"
list_of_task_files = []
file_directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)
frame.pack()




task_name = tk.Label(frame, text="Task Name")
task_name.grid(row=0, column=0, padx=10, pady=10)

task_details = tk.Label(frame, text="Task Details")
task_details.grid(row=0, column=1, padx=10, pady=10)

task_time = tk.Label(frame, text="Task Time")
task_time.grid(row=0, column=2, padx=10, pady=10)

task_list_folder = tk.Label(frame, text=os.path.dirname(os.path.realpath(current_task_file)))
task_list_folder.grid(row=0,column=4,padx=10,pady=10)


global enter_task_name
enter_task_name = tk.Entry(frame)
enter_task_name.grid(row=1,column=0,padx=10,pady=10)

global enter_task_details
enter_task_details = tk.Entry(frame)
enter_task_details.grid(row=1,column=1,padx=10,pady=10)

global enter_task_time
enter_task_time = tk.Entry(frame)
enter_task_time.grid(row=1,column=2,padx=10,pady=10)

global enter_task_list
enter_task_list = tk.Entry(frame)
enter_task_list.grid(row=1,column=4,padx=10,pady=10)

global task_email_receiver
task_email_receiver = tk.Entry(frame)
task_email_receiver.grid(row=1,column=5,padx=10,pady=10)

def send_task_list():
    global task_email_receiver
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "loyalfan82@gmail.com"
    print(task_email_receiver.get())
    receiver_email = task_email_receiver.get()
    password = "Ywngtpi1y"
    current_task_file_name = current_task_file.split("\\")[-1][0:-14]
    message = f"""\
    Subject: Task List

    You were sent the following task list for {current_task_file_name}: """
    # message = f" :"
    with open(current_task_file) as json_file:
        data = json.load(json_file)
    if type(data) is str:
        data = json.loads(data)
    for task in data['tasks']:
        print(data['tasks'].index(task))
        message +="""\n
        """
        message += f"Task {data['tasks'].index(task)+1} name: {task['name']}," \
                   f" Task {data['tasks'].index(task)+1} details: {task['details']}, " \
                   f"Task {data['tasks'].index(task)+1} time: {task['time']}"

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def delete_task_list(deleteIndex):

    os.remove(list_of_task_files[deleteIndex])
    list_of_task_files.pop(deleteIndex)
    with open(current_task_file, 'w') as outfile:
        json.dump(data, outfile)
    reset_frame()
    build_frame(data['tasks'])

def create_task_list():
    global enter_task_list
    global file_directory
    global list_of_task_files
    global frame
    if not os.path.exists(enter_task_list.get() + 'task_data.json'):
        with open(enter_task_list.get() + 'task_data.json', 'w') as outfile:
            json.dump({"tasks": []}, outfile)
        list_of_task_files = []
        for r, d, f in os.walk(file_directory):
            for file in f:
                if file.endswith("task_data.json"):
                    list_of_task_files.append(os.path.join(r, file))
        frame.destroy()
        reset_frame()
        build_frame([])

def delete_task(deleteIndex):
    with open(current_task_file) as json_file:
        data = json.load(json_file)
    if type(data) is str:
        data = json.loads(data)
    data['tasks'].pop(deleteIndex)
    with open(current_task_file, 'w') as outfile:
        json.dump(data, outfile)
    reset_frame()
    build_frame(data['tasks'])

def add_task():
    global frame
    global enter_task_time
    global enter_task_name
    global enter_task_details
    with open(current_task_file) as json_file:
        data = json.load(json_file)
    if type(data) is str:
        data = json.loads(data)
    add_data = [{'name': enter_task_name.get(),
         'details': enter_task_details.get(),
         'time': enter_task_time.get()}]

    data['tasks'] = data['tasks'] + add_data

    reset_frame()
    json_string = json.dumps(data)
    with open(current_task_file, 'w') as outfile:
        json.dump(json_string, outfile)

    with open(current_task_file) as json_file:
        data = json.load(json_file)
    data = json.loads(data)
    build_frame(data['tasks'])

def load_task_file(file_name):
    global current_task_file
    current_task_file = file_name
    frame.destroy()
    reset_frame()
    with open(current_task_file) as json_file:
        data = json.load(json_file)
        if type(data) is str:
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
    for y in range(0, len(list_of_task_files), 1):
        display_task_file = tk.Button(frame, text=list_of_task_files[y].split("\\")[-1][0:-14], command=partial(load_task_file, list_of_task_files[y]))
        display_task_file.grid(row=y+2, column=4, padx=10, pady=10)

        delete_task_file_button = tk.Button(frame, text="delete", command=partial(delete_task_list, y))
        delete_task_file_button.grid(row=y + 2, column=5, padx=10, pady=10)
        if list_of_task_files[y].split("\\")[-1][0:-14] == current_task_file.split("\\")[-1][0:-14]:
            display_task_file["state"] = "disabled"
            delete_task_file_button["state"] = "disabled"

def reset_frame():
    global frame
    global enter_task_time
    global enter_task_name
    global enter_task_details
    global enter_task_list
    global task_email_receiver
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
    enter_task_list = tk.Entry(frame)
    enter_task_list.grid(row=1, column=4, padx=10, pady=10)
    task_list_label = tk.Label(frame, text="Task List")
    task_list_label.grid(row=0,column=4,padx=10,pady=10)
    create_task_list_button = tk.Button(frame, text="Create Task List", command=create_task_list)
    create_task_list_button.grid(row=1, column=3, padx=10, pady=10)
    task_email_receiver = tk.Entry(frame)
    task_email_receiver.grid(row=1, column=5, padx=10, pady=10)
    send_email_button = tk.Button(frame, text="Send Current Task List as Email to:", command=send_task_list)
    send_email_button.grid(row=0, column=5, padx=10, pady=10)



add_task_button = tk.Button(frame,text="Add Task", command=add_task)
add_task_button.grid(row=0,column=3,padx=10,pady=10)

create_task_list_button = tk.Button(frame,text="Create Task List", command=create_task_list)
create_task_list_button.grid(row=1,column=3,padx=10,pady=10)

send_email_button = tk.Button(frame,text="Send current Task as Email to:", command=send_task_list)
send_email_button.grid(row=0,column=5,padx=10,pady=10)


if not os.path.exists('Tutorialtask_data.json'):
    with open(current_task_file, 'w') as outfile:
        json.dump({"tasks": [{"name": "Create Task List",
                              "details": "Enter the name of a to-do list in the entry below the \"Task List\" label "
                                         "and click the \"Create Task List\" button",
                              "time": "3/11/2022 5:30 PM"
                              },
                             {"name": "Send Email",
                              "details": "enter an email in the entry below the \"Send Current Task List as Email to:\" "
                                         "button",
                              "time": "3/11/2022 7:00 PM"}]}, outfile)
        with open(current_task_file) as json_file:
            data = json.load(json_file)
            if type(data) is str:
                data = json.loads(data)
            build_frame(data['tasks'])
else:
    with open(current_task_file) as json_file:
        data = json.load(json_file)
        if type(data) is str:
            data = json.loads(data)
        build_frame(data['tasks'])

for r, d, f in os.walk(file_directory):
    for file in f:
        if file.endswith("task_data.json"):
            list_of_task_files.append(os.path.join(r, file))
current_task_file = list_of_task_files[0]
load_task_file(current_task_file)

root.mainloop()
