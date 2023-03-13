import tkinter
import tkinter.messagebox
import pickle




def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task")

def load_tasks():
    tasks = pickle.load(open("tasks.txt", "rb"))
    for task in tasks:
        listbox_tasks.insert(tkinter.END, task)

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.txt", "wb"))

    # create GUI
def create_tasks():
    root = tkinter.Tk()
    root.title("To Do List")
    frame_tasks = tkinter.Frame(root)
    frame_tasks.pack()

    scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
    scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    global listbox_tasks
    listbox_tasks = tkinter.Listbox(frame_tasks, yscrollcommand=scrollbar_tasks.set, height=3, width=50)
    listbox_tasks.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    scrollbar_tasks.config(command=listbox_tasks.yview)
    global entry_task
    entry_task = tkinter.Entry(root, width=50)
    entry_task.pack()

    button_add_task = tkinter.Button(root, text="Add task", width=50, command=add_task)
    button_add_task.pack()

    button_delete_task = tkinter.Button(root, text="Delete task", width=50, command=delete_task)
    button_delete_task.pack()

    button_load_task = tkinter.Button(root, text="Load tasks", width=50, command=load_tasks)
    button_load_task.pack()

    button_save_task = tkinter.Button(root, text="Save tasks", width=50, command=save_tasks)
    button_save_task.pack()

    root.mainloop()

create_tasks()
