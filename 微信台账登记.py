import itchat
import time
from pyexcel_xls import save_data
from pyexcel_xls import get_data

# data = get_data(r"/Users/ShaoShuai/Desktop/shaunpy/微信台账登记.xls")
data = get_data(r"c:/shaunpy/微信台账登记.xls")
print(len(data['工作表1']))


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['Text'][0:3] == '流水账':
        print(msg['ActualNickName'], msg['Text'][4:])
        data['工作表1'].append(
            [msg['ActualNickName'], msg['Text'][4:], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())])
        save_data("微信台账登记.xls", data)
        return '流水账记录成功！', msg['Text']
    elif msg['Text'][0:3] == '取备件':
        print(msg['ActualNickName'], msg['Text'][4:])
        data['工作表2'].append(
            [msg['ActualNickName'], msg['Text'][4:], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())])
        save_data("微信台账登记.xls", data)
        return '备件台账记录成功！', msg['Text']


itchat.auto_login(hotReload=True)
itchat.run()
