import _tkinter
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import scrolledtext

# more classes

class App(ttk.Window):
    def __init__(self, title:str, geometry):
        # setup
        super().__init__()
        self.title(title)
        self.geometry(f"{geometry[0]}x{geometry[1]}")
        self.minsize(geometry[0], geometry[1])

        # widgets
        self.segment = Segment(self, "label", "button")
        self.segment = Segment(self, "test", "click")
        self.segment = Segment(self, "hello", "test")
        self.segment = Segment(self, "bye", "launch")
        self.segment = Segment(self, "last", "exit")


        # run
        self.mainloop()

class Segment(ttk.Frame):
    def __init__(self, parent, label_text:str, button_text:str):
        super().__init__(master=parent)

        # widgets
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")

        label = ttk.Label(self, text=label_text)
        button = ttk.Button(self, text=button_text)
        entry = Entry(self, button_text)
        label.grid(row=0, column=0, sticky="nsew")
        button.grid(row=0, column=1, sticky="nsew")
        entry.grid(row=0, column=2, sticky="nsew")

        self.pack(expand=True, fill="both", padx=10, pady=10)

class Entry(ttk.Frame):
    def __init__(self, parent, button_text1):
        super().__init__(master=parent)

        self.rowconfigure(1, weight=1)
        self.columnconfigure((0), weight=1, uniform="a")

        entry = ttk.Entry(self)
        button = ttk.Button(self, text=button_text1)
        entry.grid(row=0, column=0, sticky="nsew", padx=2, pady=5)
        button.grid(row=1, column=0, sticky="nsew", padx=2, pady=5)


App("More classes", (400, 600))
