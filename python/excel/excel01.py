import  openpyxl
wb = openpyxl.load_workbook('C:\\Users\\IBRAHIM\\Documents\\ml-vet-journey\\python\\excel\\example3.xlsx')
print(type(wb))
# Getting sheets from the workbook using get.sheet_name() method
print(wb.get_sheet_names())
sheet = wb.get_sheet_by_name('Sheet3')
print(sheet)
print(type(sheet))
print(sheet.title)

