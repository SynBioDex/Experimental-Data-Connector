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

media_options = input_metadata['media']

strain_options = input_metadata['strain']

supp_options = input_metadata['supplement']

#Next section is button management


#MEDIA SELECTION DROP DOWN
label = Label(root, text = "Select Media(s) from Menu")
label.grid(column =0, row =0, sticky=tk.N+tk.S+tk.W+tk.E)

media = tk.StringVar(root)

media.set("-Media-")

media_option = tk.OptionMenu(root, media, *media_options) #ENTER a command to reduce the selection process
media_option.grid(column =0, row =1, sticky=tk.N+tk.S+tk.W+tk.E)

temp_list =[]

#adding selections to a media list to reference later
media_list = []

def media_dropdown(*args):
    global dropdown
    dropdown = str(media.get())
    print(dropdown)

    if media.get() == media_options[0]:
        media_select = media_options[0]

    if media.get() == media_options[1]:
        media_select = media_options[1]

    media_list.append(media_select)
    result_label.config(text=f"{media_list}", fg = "blue")
    result_label.grid(column =2, row=1, sticky=tk.N+tk.S+tk.W+tk.E)

temp_list.append(media_list)

# link function to change dropdown
media_button = Button(root, text = "add", command = media_dropdown)
media_button.grid(column = 1, row =1, sticky=tk.N+tk.S+tk.W+tk.E )



#STRAIN SELECTION DROP DOWN MENU
label = Label(root, text = "Select Strain(s) from Menu")
label.grid(column =0, row =3, sticky=tk.N+tk.S+tk.W+tk.E)

strain = tk.StringVar(root)

strain.set("-Strain-")

strain_option = tk.OptionMenu(root, strain, *strain_options)
strain_option.grid(column =0, row =4, sticky=tk.N+tk.S+tk.W+tk.E)

#adding strain selections to a list to reference later
strain_list = []

def strain_dropdown(*args):
    global dropdown
    dropdown = str(strain.get())
    print(dropdown)

    if strain.get() == strain_options[0]:
        strain_select = strain_options[0]

    if strain.get() == strain_options[1]:
        strain_select = strain_options[1]

    strain_list.append(strain_select)
    sresult_label.config(text=f"{strain_list}", fg = "blue")
    sresult_label.grid(column =2, row=4, sticky=tk.N+tk.S+tk.W+tk.E)
    
temp_list.append(strain_list)

strain_button = Button(root, text = "add", command = strain_dropdown)
strain_button.grid(column = 1, row =4, sticky=tk.N+tk.S+tk.W+tk.E )



#Temp list button to check if the variables were added correctly
def temp_list1():
    print(temp_list)

temp_listbutton = Button(root, text = "temp list", command = temp_list1)
temp_listbutton.grid(column=0, row=15, sticky=tk.N+tk.S+tk.W+tk.E )
#End


#SUPPLEMENT SELECTION DROP DOWN MENU
label = Label(root, text = "Select Supplement(s) from Menu")
label.grid(column =0, row =6, sticky=tk.N+tk.S+tk.W+tk.E)

supp = tk.StringVar(root)

supp.set("-Supplement-")

supp_option = tk.OptionMenu(root, supp, *supp_options)
supp_option.grid(column =0, row =7, sticky=tk.N+tk.S+tk.W+tk.E)

#Dropdown selection loop to add the selected values to the overall temp list
supp_list = []

def supp_dropdown(*args):
    global dropdown
    dropdown = str(supp.get())
    print(dropdown)

    if supp.get() == supp_options[0]:
        supp_select = supp_options[0]

    if supp.get() == supp_options[1]:
        supp_select = supp_options[1]

    supp_list.append(supp_select)
    suresult_label.config(text=f"{supp_list}", fg = "blue")
    suresult_label.grid(column =2, row=7, sticky=tk.N+tk.S+tk.W+tk.E)

temp_list.append(supp_list)

supp_button = Button(root, text = "add", command = supp_dropdown)
supp_button.grid(column = 1, row =7, sticky=tk.N+tk.S+tk.W+tk.E )

 

#replicates enter menu
label = Label(root, text = "Enter in Number of Replicates")
label.grid(column =0, row =11, sticky=tk.N+tk.S+tk.W+tk.E)

#Back to GUI work, the following is the replicates entry field and check value button
repli_enter = Entry(root, width = 10)
repli_enter.grid(column =0, row =12, sticky=tk.N+tk.S+tk.W+tk.E)

result_label = Label(root, text = "", fg = "black")
result_label.grid(column =1, row =12)

sresult_label = Label(root, text = "", fg = "black")
sresult_label.grid(column =1, row = 13)

suresult_label = Label(root, text = "", fg = "black")
suresult_label.grid(column =1, row = 14)

'''
#ENTRY LIST CODE
entry_list = []

for entry in temp_list:
    temp_list2 = temp_list[entry]
    entry_list.append(temp_list2)


def show():
    try:
            value = int(repli_enter.get())
            combinations = list(product(*entry_list))
            print(combinations)

    except ValueError:
            result_label.config(text="Not a valid integer", fg = "red")
'''

button = Button(root, text = "Generate", command = show).grid()

label = Label(root, text = " ")
label.grid()

root.mainloop()

#EXCEL WORK BELOW
wb = Workbook()
sheet = wb.active

combinations = list(product(*entry_list))

num_copies = int(repli_enter.get())


#EXCEL LISTING CODE BELOW
for index, combination in enumerate(combinations):
    sheet[uppercase_alphabet[index]+'1'] = (f'{combination}')
    for i in range(3):
        # CHANGE THE RANGE(3) TO RANGE(REPLI_ENTER) WHEN POSSIBLE
        sheet[uppercase_alphabet[index] + str(i + 2)] = (f'{combination}')

#REMOVING AND THEN SAVING THE EXCEL TEST SHEET
filename = "excel_test_sheet.xlsx"
try:
    os.remove('./'+ filename)
except:
    pass

wb.save(filename = filename)
