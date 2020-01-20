import openpyxl
import os

book = openpyxl.load_workbook("/home/redintegro/Documents/ex.xlsx")
sheet = book.active
os.remove("/home/redintegro/Documents/ex.xlsx")