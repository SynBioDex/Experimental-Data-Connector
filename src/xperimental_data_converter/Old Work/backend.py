from openpyxl import load_workbook
from openpyxl import Workbook

from itertools import product

from tkinter import *
from tkinter import Entry, Button, messagebox
import tkinter as tk

import os
import string
uppercase_alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

from gui_new import result_label
from gui_new import input_metadata
from gui_new import media
from gui_new import media_options
from gui_new import temp_list

#The following function determines if the entered replicate value is a integer or not
#If it is, then it continues to print all of the combinations possible
#If it is not, then it prints "not a valid integer" and allows for another try

from gui_new import repli_enter

entry_list = []

for entry in input_metadata:
    temp_list2 = temp_list[entry]
    entry_list.append(temp_list2)

def show():
    try:
            value = int(repli_enter.get())
            result_label.config(text=f"Valid integer: {value}", fg = "green")
            combinations = list(product(*entry_list))
            print(combinations)

    except ValueError:
            result_label.config(text="Not a valid integer", fg = "red")

#Added the below code from og code
wb = Workbook()
sheet = wb.active

combinations = list(product(*entry_list))

'''
num_copies = int(repli_enter.get())
'''
#PROBLEM CHILD CODE BELOW
for index, combination in enumerate(combinations):
    sheet[uppercase_alphabet[index]+'1'] = (f'{combination}')
    for i in range(3):
        # Modify the row index as needed (e.g., 'A2', 'A3', etc.)
        sheet[uppercase_alphabet[index] + str(i + 2)] = (f'{combination}')
#PROBLEM CHILD CODE ENDS

filename = "excel_test_sheet.xlsx"
try:
    os.remove('./'+ filename)
except:
    pass

wb.save(filename = filename)