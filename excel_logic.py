from openpyxl import load_workbook

def from_variant(variant):
    wb = load_workbook('fam.xlsx')
    sheet = wb["Дано"]
    lst = []
    row_index = variant + 1
    for cellObj in sheet[f'A{row_index}':f'N{row_index}']:
        for cell in cellObj:
            lst.append(cell.value)
    wb.save("fam.xlsx")
    return lst
    

def to_variant(lst):
    wb = load_workbook('fam.xlsx')
    sheet = wb["Дано"]
    row_count = sheet.max_row + 1

    for i in range(len(lst)):
        sheet.cell(row = row_count, column = i+1).value = lst[i]
    
    wb.save("fam.xlsx")
