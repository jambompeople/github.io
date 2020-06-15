from tkinter import *

root = Tk()

hi = Label(root, text="hello this is working too")
hi1 = Label(root, text="hello this is working too")

hi.grid(row = 0, column = 0)
hi1.grid(row = 1, column = 0)

what = Label(root, text="what").grid(row = 2, column = 0)
what1 = Label(root, text="what in the world").grid(row = 3, column = 0)

button = Button(root, text = "click me", padx = 50, pady = 50).grid(row = 4, column = 0)
root.mainloop()
