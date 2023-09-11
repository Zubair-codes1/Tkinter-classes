import _tkinter
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import scrolledtext
from random import choice

# App
class App(ttk.Window):
    def __init__(self, title, geometry):
        super().__init__()
        # attributes
        self.title(title)
        self.geometry(f"{geometry[0]}x{geometry[1]}")

        # frame
        self.frame = ttk.Frame(self)
        self.frame.pack(expand=True, fill="both")

        # checking size and calling functions
        SizeChecker(
            self,
            {300: self.create_small_layout, 600: self.create_medium_layout, 1200: self.create_large_layout})

        self.mainloop()

    # small layout
    def create_small_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        ttk.Label(self.frame, text="Label 1", background="red").pack(expand=True, fill="both", padx=10, pady=5)
        ttk.Label(self.frame, text="Label 2", background="green").pack(expand=True, fill="both", padx=10, pady=5)
        ttk.Label(self.frame, text="Label 3", background="blue").pack(expand=True, fill="both", padx=10, pady=5)
        ttk.Label(self.frame, text="Label 4", background="yellow").pack(expand=True, fill="both", padx=10, pady=5)

        self.frame.pack(expand=True, fill="both")

    # medium layout
    def create_medium_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.columnconfigure((0, 1), weight=1, uniform="a")
        self.frame.rowconfigure((0, 1), weight=1, uniform="a")
        self.frame.pack(expand=True, fill="both")

        ttk.Label(self.frame, text="Label 1", background="red").grid(column=0, row=0, sticky="nsew", pady=5, padx=10)
        ttk.Label(self.frame, text="Label 2", background="green").grid(column=1, row=0, sticky="nsew", pady=5, padx=10)
        ttk.Label(self.frame, text="Label 3", background="blue").grid(column=0, row=1, sticky="nsew", pady=5, padx=10)
        ttk.Label(self.frame, text="Label 4", background="yellow").grid(column=1, row=1, sticky="nsew", pady=5, padx=10)

    # large layout
    def create_large_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.columnconfigure((0, 1, 2, 3), weight = 1, uniform="a")
        self.frame.rowconfigure(0, weight=1, uniform="a")
        self.frame.pack(expand=True, fill="both")

        ttk.Label(self.frame, text="Label 1", background="red").grid(column=0, row=0, sticky="nsew", pady=5, padx=10)
        ttk.Label(self.frame, text="Label 2", background="green").grid(column=1, row=0, sticky="nsew", pady=5, padx=10)
        ttk.Label(self.frame, text="Label 3", background="blue").grid(column=2, row=0, sticky="nsew", pady=5, padx=10)
        ttk.Label(self.frame, text="Label 4", background="yellow").grid(column=3, row=0, sticky="nsew", pady=5, padx=10)


# To check window size for adjustments
class SizeChecker:
    def __init__(self, window, size_dict):
        self.window = window
        # sorted dictionary of the geometry
        self.size_dict = {key: value for key, value in sorted(size_dict.items())}
        self.current_min_size = None
        self.window.bind("<Configure>", self.check_size)
        self.window.update()
        
        # maxsize
        self.window.minsize(400, 300)

    def check_size(self, event):
        if event.widget == self.window:
            window_width = event.width
            checked_size = None

            for min_size in self.size_dict:
                change = window_width - min_size
                if change >= 0:
                     checked_size = min_size

            if checked_size != self.current_min_size:
                self.current_min_size = checked_size
                self.size_dict[self.current_min_size]()

app = App("Responsive layouts", [400, 400])
