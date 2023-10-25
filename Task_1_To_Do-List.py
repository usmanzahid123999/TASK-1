import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task = task_list.get(task_list.curselection())
        task_list.delete(task_list.curselection())
    except:
        pass


root = tk.Tk()# Creating the main window
root.title("To-Do List")


task_list = tk.Listbox(root)#creating listbox for task which we have added
task_list.pack(pady=10)


task_entry = tk.Entry(root, width=40)#adding task
task_entry.pack()

# Create buttons for adding and deleting tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()


root.mainloop()
