from openpyxl import Workbook

'''
    pip install openpyxl

'''

wb = Workbook()
ws = wb.active

ws.title = "내시트"
wb.save("sample.xlsx")
wb.close()
