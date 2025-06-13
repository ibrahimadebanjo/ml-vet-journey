import openpyxl 
wb = openpyxl.load_workbook('C:\\Users\\IBRAHIM\\Documents\\ml-vet-journey\\python\\excel\\example3.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
print(tuple(sheet['A1':'C3']))
for rowOfCellObjects in sheet['A1':'C3']:
     for cellObj in rowOfCellObjects:
            print(cellObj.coordinate, cellObj.value)
     print('--- END OF ROW ---')
