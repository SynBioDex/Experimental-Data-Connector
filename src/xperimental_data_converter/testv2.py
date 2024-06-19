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

'''
print(combinations)
'''

for index, combination in enumerate(combinations):
    for cindex in range(0,3):
        sheet[uppercase_alphabet[cindex]+str(index+1)] = (f'{combination[cindex]}')
filename = "excel_test_sheet.xlsx"
try:
    os.remove('./'+filename)
except:
    pass
wb.save(filename = filename)