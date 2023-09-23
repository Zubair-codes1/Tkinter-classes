import tkinter as tk
from tkinter import ttk
from random import randint, choice

window = tk.Tk()
window.geometry("600x400")
window.title("Scrollable")

# widgets
canvas = tk.Canvas(window, bg="white", scrollregion=(0, 0, 2000, 5000)) # (l, t, r, b)
canvas.create_line(0, 0, 2000, 5000, fill="blue", width=10)
for i in range(100):
    left = randint(0, 2000)
    top = randint(0, 5000)
    right = left + randint(10, 500)
    bottom = top + randint(10, 500)
    color = choice(("red", "green", "yellow", "orange"))
    canvas.create_rectangle(left, top, right, bottom, fill=color)
canvas.pack(expand=True, fill="both")

# mousewheel scrolling vertical
canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(-int(event.delta / 60), "units"))

# mousewheel scrolling horizontal
canvas.bind("<Control MouseWheel>", lambda event: canvas.xview_scroll(-int(event.delta/60), "units"))

# scrollbar - vertical
scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set) # changes the position of scroll bar based on how much is scrolled
scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")

# scrollbar - horizontal
scrollbar_horizontal = ttk.Scrollbar(window, orient="horizontal", command=canvas.xview)
canvas.configure(xscrollcommand=scrollbar_horizontal.set)
scrollbar_horizontal.place(relx=0, rely=1, relwidth=1, anchor="sw")

# run
window.mainloop()
