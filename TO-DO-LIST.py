import os
import tkinter as tk
from tkinter import messagebox, simpledialog

# Define the filename where tasks will be saved
FILENAME = 'tasks.txt'

# Load tasks from the file
def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            tasks = [line.strip() for line in file]
    return tasks

# Save tasks to the file
def save_tasks(tasks):
    with open(FILENAME, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Add a task to the list
def add_task():
    task = simpledialog.askstring("Add Task", "Enter the task:")
    if task:
        tasks.append(task)
        update_task_list()
        save_tasks(tasks)
        messagebox.showinfo("Success", f"Task '{task}' added.")

# View all tasks in the list
def view_tasks():
    if not tasks:
        messagebox.showinfo("Tasks", "No tasks in the list.")
    else:
        task_list.delete(0, tk.END)
        for i, task in enumerate(tasks, 1):
            task_list.insert(tk.END, f"{i}. {task}")

# Delete a task from the list
def delete_task():
    try:
        selected_index = task_list.curselection()[0]
        task = tasks.pop(selected_index)
        update_task_list()
        save_tasks(tasks)
        messagebox.showinfo("Success", f"Task '{task}' deleted.")
    except IndexError:
        messagebox.showerror("Error", "Please select a task to delete.")

# Update the task list in the GUI
def update_task_list():
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks, 1):
        task_list.insert(tk.END, f"{i}. {task}")

# Main function to run the application
def main():
    global tasks, task_list

    tasks = load_tasks()

    # Create the main window
    root = tk.Tk()
    root.title("To-Do List Application")

    # Create and pack the task list
    task_list = tk.Listbox(root, width=50, height=15)
    task_list.pack(pady=10)

    # Create and pack the buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    add_button = tk.Button(button_frame, text="Add Task", command=add_task)
    add_button.grid(row=0, column=0, padx=5)

    view_button = tk.Button(button_frame, text="View Tasks", command=view_tasks)
    view_button.grid(row=0, column=1, padx=5)

    delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
    delete_button.grid(row=0, column=2, padx=5)

    exit_button = tk.Button(button_frame, text="Exit", command=root.quit)
    exit_button.grid(row=0, column=3, padx=5)

    # Populate the task list with existing tasks
    update_task_list()

    # Run the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()
