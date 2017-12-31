from fuzzywuzzy import fuzz
from pyexcel_xls import get_data

xlsx = get_data(r"/Users/ShaoShuai/Desktop/ss.xlsx")
flag = 0
value = 0
valuelist = []
name = input('请输入设备模糊名称或缺陷信息:\n')

for flag in range(len(xlsx['工作表1'])):
    valuelist.append(fuzz.partial_ratio(str(xlsx['工作表1'][flag][0]), name))
    flag = flag + 1

for i in range(len(valuelist)):
    for j in range(i + 1, len(valuelist)):
        if valuelist[i] < valuelist[j]:
            valuelist[i], valuelist[j] = valuelist[j], valuelist[i]
            xlsx['工作表1'][i][0], xlsx['工作表1'][j][0] = xlsx['工作表1'][j][0], xlsx['工作表1'][i][0]

if valuelist[0] >= 40:
    print('\n匹配度前五名为：\n')
    for k in range(5):
        if valuelist[k] >= 20:
            print(k + 1, xlsx['工作表1'][k][0], ' 相似度:', valuelist[k], '%')
    choose = int(input('\n请输入您要查看信息的设备编号（1~5）:\n'))
    print('设备名称：', str(xlsx['工作表1'][choose - 1][0]))
    print('设备KKS编码：', str(xlsx['工作表1'][choose - 1][1]))
    print('设备类型：', str(xlsx['工作表1'][choose - 1][2]))
    print('设备型号规格：', str(xlsx['工作表1'][choose - 1][3]))
    print('设备安装位置：', str(xlsx['工作表1'][choose - 1][4]))
else:
    print('抱歉，未检索到匹配设备信息！')
