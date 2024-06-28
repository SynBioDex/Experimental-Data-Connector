from openpyxl import load_workbook
from openpyxl import Workbook

from itertools import product

from tkinter import *
from tkinter import Entry, Button, messagebox
import tkinter as tk

root = tk.Tk()
root.title("Welcome to LabGen")
root.geometry("500x500")

repli_enter = Entry(root, width = 10)
repli_enter.grid(column =0, row =12, sticky=tk.N+tk.S+tk.W+tk.E)

result_label = Label(root, text = "", fg = "black")
result_label.grid(column =1, row =12)

def show():
    try:
            value = int(repli_enter.get())
            result_label.config(text=f"Valid integer: {value}", fg = "green")
    except ValueError:
            result_label.config(text="Not a valid integer", fg = "red")

button = Button(root, text = "Generate", command = show).grid()

label = Label(root, text = " ")
label.grid()


root.mainloop()