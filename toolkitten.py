from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)

root.mainloop()