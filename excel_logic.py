from openpyxl import load_workbook

wb = load_workbook('fam.xlsx')
sheet = wb["Дано"]

def from_variant(variant):
    lst = []
    row_index = variant + 1
    for cellObj in sheet[f'B{row_index}':f'O{row_index}']:
        for cell in cellObj:
            lst.append(cell.value)
    return lst
