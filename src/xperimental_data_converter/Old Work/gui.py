from openpyxl import load_workbook
from openpyxl import Workbook

from itertools import product

from tkinter import *
from tkinter import Entry, Button, messagebox
import tkinter as tk

import os
import string
uppercase_alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]


#dictionary has strain, media, chemical, supplement
input_metadata_test = {
                'media':['lb', 'm9'],
                'strain':['top10', 'dh5a'],
                'supplement':['atc', 'iptg']
                }

'''
'vector':['repressilator','toggleswitch'],
                'replicates':[i+1 for i in range(10)]
''' 

#gui work below
root = tk.Tk()
root.title("Welcome to LabGen")
root.geometry("500x500")

#List of options for each variable
media_options = input_metadata_test['media']

strain_options = input_metadata_test['strain']

supp_options = input_metadata_test['supplement']

#vector_options = input_metadata['vector']

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

#Back to GUI work, the following is the replicates entry field and check value button
repli_enter = Entry(root, width = 10)
repli_enter.grid(column =0, row =12, sticky=tk.N+tk.S+tk.W+tk.E)

result_label = Label(root, text = "", fg = "black")
result_label.grid(column =1, row =12)

#The following function determines if the entered replicate value is a integer or not
#If it is, then it continues to print all of the combinations possible
#If it is not, then it prints "not a valid integer" and allows for another try
entry_list = []

label = Label(root, text = " ")
label.grid()

#Excel sheet opening work
def generate(input_metadata):
    wb = Workbook()
    sheet = wb.active

    entry_list = []

    for entry in input_metadata:
        temp_list = input_metadata[entry]
        entry_list.append(temp_list)

    print(entry_list)

    combinations = list(product(*entry_list))
    #num_copies = int(repli_enter.get())

    #PROBLEM CHILD CODE BELOW
    for index, combination in enumerate(combinations):
        sheet[uppercase_alphabet[index]+'1'] = (f'{combination}')
        for i in range(4):
            # Modify the row index as needed (e.g., 'A2', 'A3', etc.)
            sheet[uppercase_alphabet[index] + str(i + 2)] = (f'{combination}')
    #PROBLEM CHILD CODE ENDS

    filename = "excel_test_sheet.xlsx"
    try:
        os.remove('./'+ filename)
    except:
        pass

    wb.save(filename = filename)
button = Button(root, text = "Generate", command = generate).grid()

generate(input_metadata_test)

root.mainloop()