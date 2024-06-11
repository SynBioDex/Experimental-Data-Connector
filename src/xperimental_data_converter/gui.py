from tkinter import *

root = Tk()

root.title("Welcome to LabGen")

root.geometry('350x200')

lbl = Label(root, text = "Enter in Lab Testing Parameters")
lbl.grid()

def printValue():
    dentry = data_num.get()
    Label(root, text=f'{dentry}, Entered', pady=20, bg='#ffbf00')

data_num = Entry(root, width = 10)
data_num.grid(column = 1, row = 0)

btn = Button(
    root,
    text = "Enter",
    fg = "blue",
    command = printValue
)

btn.grid(column = 2, row = 0)

root.mainloop()