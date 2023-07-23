import openpyxl

file = "C:/Development/robot-scripts/SeleniumWithPython/Data.xlsx"

workbook = openpyxl.load_workbook(file)

sheet = workbook["Sheet2"]


for r in range(1,6):
    for c in range(1,4):
        sheet.cell(r,c).value = "Welcome"
workbook.save(file)
