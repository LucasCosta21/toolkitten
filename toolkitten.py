from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

globalTaskCount = 0

def addTask(frm, text):
    ttk.Label(frm, text=text).grid(row=2, column=2)

newTask = ttk.Entry(frm)
newTask.grid(column=0, row=0)
ttk.Button(frm, text="add new task", command=addTask(frm, newTask)).grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)

root.mainloop()

# class cTodo:
#     task = []

#     def __init__(self, frm):
#         text =
#         ttk.Button(frm, text="add new task", command=self.addTask()).grid(column=1, row=0)

#     def addTask(self, text):
#         self.task.add(text)

