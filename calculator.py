from tkinter import*

root = Tk()
root.title("calculator")
ent = Entry(root, width = 35, borderwidth = 5)
ent.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
#create buttons
button1 = Button(root, text = "1", padx = 40, pady = 20, command = buttonadd)
button2 = Button(root, text = "2", padx = 40, pady = 20, command = buttonadd)
button3 = Button(root, text = "3", padx = 40, pady = 20, command = buttonadd)
button4 = Button(root, text = "4", padx = 40, pady = 20, command = buttonadd)
button5 = Button(root, text = "5", padx = 40, pady = 20, command = buttonadd)
button6 = Button(root, text = "6", padx = 40, pady = 20, command = buttonadd)
button7 = Button(root, text = "7", padx = 40, pady = 20, command = buttonadd)
button8 = Button(root, text = "8", padx = 40, pady = 20, command = buttonadd)
button9 = Button(root, text = "9", padx = 40, pady = 20, command = buttonadd)
button0 = Button(root, text = "0", padx = 40, pady = 20, command = buttonadd)
buttonequal = Button(root, text = "=", padx = 40, pady = 20, command = buttonadd)
buttonplus = Button(root, text = "+", padx = 40, pady = 20, command = buttonadd)
buttonminus = Button(root, text = "-", padx = 40, pady = 20, command = buttonadd)
buttontimes = Button(root, text = "*", padx = 40, pady = 20, command = buttonadd)
buttondivide = Button(root, text = "/", padx = 40, pady = 20, command = buttonadd)
#put the buttons on the screen
button1.grid(row = 3, column = 0)
button2.grid(row = 3, column = 1)
button3.grid(row = 3, column = 2)

button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button5.grid(row = 2, column = 2)

button7.grid(row = 1, column = 0)
button8.grid(row = 1, column = 1)
button9.grid(row = 1, column = 2)

button0.grid(row = 4, column = 0)

#buttonequal.grid(row = , column = )
#buttonplus.grid(row = , column = )
#buttonminus.grid(row = , column = )
#buttontimes.grid(row = , column = )
#buttondivide.grid(row = , column = )
root.mainloop()
