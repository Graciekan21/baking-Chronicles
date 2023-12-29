# Import module
import tkinter
import tkinter.messagebox

# Function to capture a task
def capture_task():
    task = input('Enter your task: ')
    task_list.append(task)
    print('Task captured successfully!')

# The app title
window = tkinter.Tk()
window.title('Bakers-to-do-list')

# Create a Frame for the Tasks
task_frame = tkinter.task_frame(window)
task_frame.pack()

window.mainloop()