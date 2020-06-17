from tkinter import *

root = Tk()

todolist = Label(root, text = "To-Do List").pack()
i = Entry(root).pack()
def add():
    task = Label(root, text = i.get())
    task.pack()

addTask = Button(root, text = "Add Task", command = add).pack()
deleteTask = Button(root, text = "Delete Task").pack()
deleteAllTask = Button(root, text = "Delete All Task").pack()
completeTask = Button(root, text = "Complete Task").pack()

root.mainloop()
