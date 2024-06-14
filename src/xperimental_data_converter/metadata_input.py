from openpyxl import load_workbook
from openpyxl import Workbook

from itertools import product

from tkinter import *
from tkinter import Entry, Button, messagebox
import tkinter as tk


#dictionary has strain, media, chemical, supplement
input_metadata = {
                'media':['lb', 'm9'],
                'strain':['top10', 'dh5a'],
                'supplement':['atc', 'iptg']
                }

#gui work below
root = tk.Tk()
root.title("Welcome to LabGen")
root.geometry("500x500")

def show():
    label.config(text = media.get())

#List of options for each variable
media_list = input_metadata['media']
media_options = [
    media_list[0],
    media_list[1]
]    

strain_list = input_metadata['strain']
strain_options = [
    strain_list[0],
    strain_list[1]
]

supp_list = input_metadata['supplement']
supp_options = [
    supp_list[0],
    supp_list[1]
]

#Next section is button management

#media selection drop down menu
label = Label(root, text = "Select Media(s) from Menu")
label.grid(column =0, row =0, sticky=tk.N+tk.S+tk.W+tk.E)

media = tk.StringVar(root)
media2 = tk.StringVar(root)

media.set("-Media-")

media_option = tk.OptionMenu(root, media, *media_options)
media_option.grid(column =0, row =1, sticky=tk.N+tk.S+tk.W+tk.E)

media2.set("-Media 2-")

media_option2 = tk.OptionMenu(root, media2, *media_options)
media_option2.grid(column =1, row =1, sticky=tk.N+tk.S+tk.W+tk.E)

#strain selection drop down menu
label = Label(root, text = "Select Strain(s) from Menu")
label.grid(column =0, row =3, sticky=tk.N+tk.S+tk.W+tk.E)

strain = tk.StringVar(root)
strain2 = tk.StringVar(root)

strain.set("-Strain-")

strain_option = tk.OptionMenu(root, strain, *strain_options)
strain_option.grid(column =0, row =4, sticky=tk.N+tk.S+tk.W+tk.E)

strain2.set("-Strain 2-")

strain_option2 = tk.OptionMenu(root, strain2, *strain_options)
strain_option2.grid(column =1, row =4, sticky=tk.N+tk.S+tk.W+tk.E)

#supplement selection drop down menu
label = Label(root, text = "Select Supplement(s) from Menu")
label.grid(column =0, row =6, sticky=tk.N+tk.S+tk.W+tk.E)

supp = tk.StringVar(root)
supp2 = tk.StringVar(root)

supp.set("-Supplement-")

supp_option = tk.OptionMenu(root, supp, *supp_options)
supp_option.grid(column =0, row =7, sticky=tk.N+tk.S+tk.W+tk.E)

supp2.set("-Supplement 2-")

supp_option2 = tk.OptionMenu(root, supp2, *supp_options)
supp_option2.grid(column =1, row =7, sticky=tk.N+tk.S+tk.W+tk.E)

#replicates enter menu
label = Label(root, text = "Enter in Number of Replicates")
label.grid(column =0, row =11, sticky=tk.N+tk.S+tk.W+tk.E)

'''
#This is a loop to chcek if the repli_enter value is an integer
def check_value():
        try:
            value = int(repli_enter.get())
            result_label.config(text=f"Valid integer: {value}", fg = "green")
        except ValueError:
            result_label.config(text="Not a valid integer", fg = "red")
'''

#Back to GUI work, the following is the replicates entry field and check value button
repli_enter = Entry(root, width = 10)
repli_enter.grid(column =0, row =12, sticky=tk.N+tk.S+tk.W+tk.E)

'''
button_print = Button(root, text = "Check value", command = check_value)
button_print.grid(column =1, row =13)
'''

result_label = Label(root, text = "", fg = "black")
result_label.grid(column =1, row =12)

#The generation of all possible combinations
entry_list = []

for entry in input_metadata:
    temp_list = input_metadata[entry]
    entry_list.append(temp_list)

#The following function determines if the entered replicate value is a integer or not
#If it is, then it continues to print all of the combinations possible
#If it is not, then it prints "not a valid integer" and allows for another try
def show():
    try:
            value = int(repli_enter.get())
            result_label.config(text=f"Valid integer: {value}", fg = "green")
            combinations = list(product(*entry_list))
            print(combinations)

    except ValueError:
            result_label.config(text="Not a valid integer", fg = "red")

button = Button(root, text = "Generate", command = show).grid()

label = Label(root, text = " ")
label.grid()

root.mainloop()

#Excel sheet opening work
cell_count = "96"
wb = Workbook()

wb["Sheet"].title = "Laboratory Generation Sheet"

ws1 = wb["Laboratory Generation Sheet"]
ws1["A1"] = "Laboratory Generation for "

strain = ["lb", "m9"]

row_start = 3
col_start = 2

for i in range(len(strain)):
    ws1.cell(row = row_start + i, column = col_start).value = strain[i]

wb.save("excel_test_sheet1.xlsx")
