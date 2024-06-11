from openpyxl import load_workbook
from itertools import product

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

print(combinations)

'''
import fileinput

filename = 'gui.py'

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
