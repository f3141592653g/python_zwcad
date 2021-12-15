import openpyxl
import contants
import os
import math
workbook = openpyxl.load_workbook(contants.excel_path)
sheet = workbook['Sheet1']
screen = sheet['D']
row_lst = []
count = 0
for cell in screen:
    if cell.value == None:
        count+=1
        # print(cell.row)
        scriptName = sheet.cell(cell.row,1).value

        path = 'D:/regress/SmokeScr'
        # print("aaa:{}".format(path))
        files = os.listdir(path)

        for f in files:
            if f == scriptName:
                row_lst.append(f)

allot_num = count / 2
allot_num = math.ceil(allot_num)
# print(allot_num)

# print(count)
# print(row_lst)
for i in range(1,3):

    count = len(row_lst) # 文件行数
    print('源文件数据行数：',count)
    # 切分diff
    diff_match_split = [row_lst[i:i+5000] for i in range(0,len(row_lst),5000)]# 每个文件的数据行数

    # 将切分的写入多个txt中
    for i,j in zip(range(0,int(count/5000+1)),range(0,int(count/5000+1))): # 写入txt，计算需要写入的文件数
        with open('D:/regress' + '/' + str(i)  + '.lst',"a") as temp:
            for line in diff_match_split[i]:
                temp.write(line)
    print('拆分后文件的个数：',i+1)
