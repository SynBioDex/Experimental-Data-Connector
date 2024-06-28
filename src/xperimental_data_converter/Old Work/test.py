from openpyxl import load_workbook
from openpyxl import Workbook

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
for combination in combinations:
    print(f'{combination[0]} in position 1')
    print(f'{combination[1]} in position 2')
    print(f'{combination[2]} in position 3')
'''

cell_count = "96"
wb = Workbook()
sheet = wb.active

wb["Sheet"].title = "Laboratory Generation Sheet"

ws1 = wb["Laboratory Generation Sheet"]
ws1["A1"] = "Laboratory Generation for "

for combination in combinations:
    sheet["A1"] = (f'{combination[0]} in position 1')
    sheet["B1"] = (f'{combination[1]} in position 2')
    sheet["C1"] = (f'{combination[2]} in position 3')

'''
wb.save("excel_test_sheet1.xlsx")
'''