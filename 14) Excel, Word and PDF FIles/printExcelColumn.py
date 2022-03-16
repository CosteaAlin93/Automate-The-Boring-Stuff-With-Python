import openpyxl
import os
os.chdir('/home/alin/Documents/Automate-The-Boring-Stuff-With-Python/14) Excel, Word and PDF FIles')
file = openpyxl.load_workbook('Second_Modified.xlsx')
sheetinfile = file.get_sheet_by_name('First')

for i in range(1, 10):
    print(i, sheetinfile.cell(row=i, column=3).value)