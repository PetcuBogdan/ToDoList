from tkinter import *
import tkinter
import os
import re
import pickle

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(END, task)
        entry_task.delete(0, END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task")

def load_tasks():
    tasks = pickle.load(open(username1+"data", "rb"))
    for task in tasks:
        listbox_tasks.insert(END, task)

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open(username1+"data", "wb"))

    # create GUI
def create_tasks():
    root = tkinter.Tk()
    root.title("To Do List")
    frame_tasks = Frame(root)
    frame_tasks.pack()

    scrollbar_tasks = Scrollbar(frame_tasks)
    scrollbar_tasks.pack(side=RIGHT, fill= Y)
    global listbox_tasks
    listbox_tasks = Listbox(frame_tasks, yscrollcommand=scrollbar_tasks.set, height=3, width=50)
    listbox_tasks.pack(side = LEFT, fill = BOTH)
    scrollbar_tasks.config(command=listbox_tasks.yview)
    global entry_task
    entry_task = Entry(root, width=50)
    entry_task.pack()

    button_add_task = Button(root, text="Add task", width=50, command=add_task)
    button_add_task.pack()

    button_delete_task = Button(root, text="Delete task", width=50, command=delete_task)
    button_delete_task.pack()

    button_load_task = Button(root, text="Load tasks", width=50, command=load_tasks)
    button_load_task.pack()

    button_save_task = Button(root, text="Save tasks", width=50, command=save_tasks)
    button_save_task.pack()

    root.mainloop()


def register_user():

    username_info = username.get()
    password_info = password.get()
    list_of_files = os.listdir()
    if username_info in list_of_files:
        username_entry.delete(0, END)
        Label(screen1, text="Username already exists", fg="red", font=("calibri", 11)).pack()
    else:
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)
        if re.search(pat, password_info):
            file = open(username_info, "w")
            file.write(username_info+"\n")
            file.write(password_info)
            file.close()
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            Label(screen1, text="Registration Success", fg="green", font=("calibri", 11)).pack()
        else:
            Label(screen1, text="Password should contain more than 8 characters,", fg="red", font=("calibri", 11)).pack()
            Label(screen1, text="a number and at least 1 special charater", fg="red", font=("calibri", 11)).pack()
            password_entry.delete(0, END)



def  register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()
    username_entry = StringVar()
    password_entry = StringVar()

    Label(screen1, text = "Please enter details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text="").pack()
    button_register = Button(screen1, text = "Register", width = 10, height = 1, command  = register_user)
    button_register.pack()

def login_user():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            Label(screen2, text="Login Success", fg="green", font=("calibri", 11)).pack()
            screen.destroy()
            create_tasks()
        else:
            Label(screen2, text="Wrong Password", fg="red" , font=("calibri", 11)).pack()
    else:
        Label(screen2, text="User not found!", fg="red", font=("calibri", 11)).pack()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_entry1
    global password_entry1
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    button_login = Button(screen2, text="Login", width=10, height=1, command=login_user)
    button_login.pack()


global screen

screen = Tk()
screen.geometry("30x250")
screen.title("To do list")
Label(text = "To do list", bg = "grey", width = "300", height = "2", font = ("Calibri",13)).pack()
Label(text = "").pack()
Button(text = "Login", height = "2", width = "30", command  = login).pack()
Label(text = "").pack()
Button(text = "Register", height = "2", width = "30", command = register).pack()
screen.mainloop()


