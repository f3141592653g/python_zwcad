import openpyxl
import contants
import os
import math

workbook = openpyxl.load_workbook(contants.excel_path)
sheet = workbook['Sheet1']
screen = sheet['D']
row_lst = []
count = 0
ips = ['123', '456']
for cell in screen:
    if cell.value == None:
        count += 1
        # print(cell.row)
        scriptName = sheet.cell(cell.row, 1).value

        path = 'D:/regress/SmokeScr'
        # print("aaa:{}".format(path))
        files = os.listdir(path)

        for f in files:
            if f == scriptName:
                row_lst.append(f)

allot_num = count / len(ips)
allot_num = math.ceil(allot_num)
row_lst_news = [row_lst[i:i + allot_num] for i in range(0, len(row_lst), allot_num)]
print(row_lst_news)
# print(allot_num)
for index, ip in enumerate(ips):
    with open("D:/regress" + "/" + "%s.lst" % ip, "w") as f:
        lists = [x + "\n" for x in row_lst_news[index]]
        f.writelines(lists)

