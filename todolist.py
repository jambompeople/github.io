from tkinter import *

root = Tk()
todolist = Label(root, text = "To-Do List")
todolist.pack()
ent = Entry(root)
ent.pack()
def add():
    task = Label(root, text = ent.get())
    task.pack()
addTask = Button(root, text = "Add Task", command = add)
addTask.pack()
deleteTask = Button(root, text = "Delete Task")
deleteTask.pack()
deleteAllTask = Button(root, text = "Delete All Task")
deleteAllTask.pack()
completeTask = Button(root, text = "Complete Task")
completeTask.pack()

root.mainloop()
