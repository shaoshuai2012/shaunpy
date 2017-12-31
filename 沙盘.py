import pyexcel_xls
from pyexcel_xls import save_data
from pyexcel_xls import get_data

data = get_data(r"/Users/ShaoShuai/Desktop/test.xlsx")
print(len(data['工作表1']))
data['工作表1'].append(['666'])
print(len(data['工作表1']))
save_data("your_file.xls", data)
