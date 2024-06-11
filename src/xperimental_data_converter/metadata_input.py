# Rosalie code
from openpyxl import load_workbook
from itertools import product
from tkinter import *
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

label = Label(root, text = "Select Media from Menu")
label.pack()
#media selection drop down menu
media = tk.StringVar(root)

media.set("-Media-")

media_option = tk.OptionMenu(root, media, *media_options)
media_option.pack()

label = Label(root, text = "Select Strain from Menu")
label.pack()
#strain selection drop down menu
strain = tk.StringVar(root)

strain.set("-Strain-")

strain_option = tk.OptionMenu(root, strain, *strain_options)
strain_option.pack()

label = Label(root, text = "Select Supplement from Menu")
label.pack()
#supplement selection drop down menu
supp = tk.StringVar(root)

supp.set("-Supplement-")

supp_option = tk.OptionMenu(root, supp, *supp_options)
supp_option.pack()

#replicates enter menu
label = Label(root, text = "Enter in Number of Replicates")
label.pack()
repli_enter = Entry(root, width = 10)
repli_enter.pack()

label = Label(root, text = " ")
label.pack()

button = Button(root, text = "Generate", command = show).pack()

label = Label(root, text = " ")
label.pack()

root.mainloop()

#placeholder for dictionary in case it needs to be moved back


entry_list = []

for entry in input_metadata:
    temp_list = input_metadata[entry]
    entry_list.append(temp_list)

combinations = list(product(*entry_list))

print(combinations)

'''
import fileinput

filename = 'test.py'

for line in fileinput.input(files = filename):
    print(line, end = '')

book = load_workbook('test sheet.xlsx')

sheet = book.active

new_data = [entry_list[0], entry_list[1], entry_list[2]]

for row in sheet['b5':'f5']:
    for index, cell in enumerate(row):
        cell.value = new_data[index]

book.save('new_test.xlsx')
'''
