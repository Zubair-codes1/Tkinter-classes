import _tkinter
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import scrolledtext

class App(ttk.Window): # inherits from ttk.Window
    def __init__(self, title, geometry):

        # main setup
        super().__init__()
        self.title = title # title of the window
        self.geometry(f"{geometry[0]}x{geometry[1]}") # getting geometry
        self.minsize(geometry[0], geometry[1]) # minimum size

        # widgets
        self.menu = Menu(self) # takes self(App class) as the parent
        self.main = Main(self)

        # run
        self.mainloop()

# menu
class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=0.3, relheight=1) # placing the label

        self.create_widgets()

    # creating the widgets
    def create_widgets(self):
        menu_button1 = ttk.Button(self, text="Button 1")
        menu_button2 = ttk.Button(self, text="Button 2")
        menu_button3 = ttk.Button(self, text="Button 3")

        menu_slider1 = ttk.Scale(self, orient="vertical")
        menu_slider2 = ttk.Scale(self, orient="vertical")

        toggle_frame = ttk.Frame(self)
        menu_toggle1 = ttk.Checkbutton(toggle_frame, text="Check 1")
        menu_toggle2 = ttk.Checkbutton(toggle_frame, text="Check 1")

        entry = ttk.Entry(self)

        # creating the grid
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

        menu_button1.grid(row=0, column=0, sticky="nswe", columnspan=2)
        menu_button2.grid(row=0, column=2, sticky="nswe")
        menu_button3.grid(row=1, column=0, columnspan=3, sticky="nswe")

        menu_slider1.grid(row=2, column=0, rowspan=2, sticky="nswe", pady=20)
        menu_slider2.grid(row=2, column=2, rowspan=2, sticky="nswe", pady=20)

        toggle_frame.grid(row=4, column=0, columnspan=3, sticky="nswe")
        menu_toggle1.pack(side="left", expand=True)
        menu_toggle2.pack(side="left", expand=True)

        entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor="center")

class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
        Entry(self, "Entry 1", "Button 1", "Green")
        Entry(self, "Entry 2", "Button 2", "Blue")

class Entry(ttk.Frame):
    def __init__(self, parent, label_text:str, button_text:str, label_background:str):
        super().__init__(parent)

        label = ttk.Label(self, textvariable=label_text, background=label_background)
        button = ttk.Button(self, text=button_text)

        label.pack(expand=True, fill="both")
        button.pack(expand=True, fill="both", pady=10)
        self.pack(side="left", expand=True, fill="both", padx=20, pady=20)


App("Class based app", (600,600))
