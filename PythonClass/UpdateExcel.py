import openpyxl

book = openpyxl.load_workbook("/home/redintegro/Documents/dev.xlsx")
sheet = book.active
cell=sheet.cell(row=2,column=1)
cell.value="hema"
book.save("/home/redintegro/Documents/dev.xlsx")