import itchat
import time
from pyexcel_xls import save_data
from pyexcel_xls import get_data

# data = get_data(r"/Users/ShaoShuai/Desktop/shaunpy/微信台账登记.xls")
data = get_data(r"C:/shaunpy/微信台账登记.xlsx")
print('流水账条数：', len(data['流水账']) - 1, '\n备件台账条数', len(data['备件台账']) - 1)


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['Text'][0:3] == '流水账':
        print(msg['ActualNickName'], msg['Text'][4:])
        data['流水账'].append(
            [msg['ActualNickName'], msg['Text'][4:], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())])
        save_data("微信台账登记.xls", data)
        return '流水账记录成功！', msg['Text']
    elif msg['Text'][0:3] == '取备件':
        print(msg['ActualNickName'], msg['Text'][4:])
        data['备件台账'].append(
            [msg['ActualNickName'], msg['Text'][4:-2], msg['ActualNickName'], msg['Text'][-2:], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())])
        save_data("微信台账登记.xls", data)
        return '备件台账记录成功！', msg['Text']


itchat.auto_login(hotReload=True)
itchat.run()
