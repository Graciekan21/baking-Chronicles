# Import module
import tkinter as tk 
import tkinter.messagebox

# App frame box
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()



