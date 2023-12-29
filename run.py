# Import module
from tkinter import *
from tkinter import messagebox

# Function to capture a task
def capture_task():
    task = input('Enter your task: ')
    task_list.append(task)
    print('Task captured successfully!')

# The main
window = tkinter.tk()
window.title('Baking-Chronicles-to-do-list')

window.mainloop()