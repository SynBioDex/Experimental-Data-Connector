from openpyxl import load_workbook
from openpyxl import Workbook

import os
import string
uppercase_alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

from itertools import product

wb = Workbook()
sheet = wb.active

#dictionary has strain, media, chemical, supplement
input_metadata = {
                'media':['lb', 'm9'],
                'strain':['top10', 'dh5a'],
                'supplement':['atc', 'iptg']
                }

#Have list entries pre-exist inside a drop down database to select from

entry_list = []

for entry in input_metadata:
    temp_list = input_metadata[entry]
    entry_list.append(temp_list)

combinations = list(product(*entry_list))
num_copies = repli_enter
'''
print(combinations)
'''

for index, combination in enumerate(combinations):
    sheet[uppercase_alphabet[index]+'1'] = (f'{combination}')
    for i in range(num_copies):
        # Modify the row index as needed (e.g., 'A2', 'A3', etc.)
        sheet[uppercase_alphabet[index] + str(i + 2)] = f'{combination}


filename = "excel_test_sheet.xlsx"

try:
    os.remove('./'+filename)
except:
    pass

wb.save(filename = filename)