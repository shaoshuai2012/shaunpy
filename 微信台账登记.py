import itchat
from pyexcel_xls import save_data
from pyexcel_xls import get_data

data = get_data(r"/Users/ShaoShuai/Desktop/test.xlsx")
data['工作表1'].append(['666'])
print(len(data['工作表1']))


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    if msg['Text'][0:3] == '流水账':
        print(msg['Text'][4:], (itchat.search_friends(userName=msg['FromUserName']))["NickName"])
        data['工作表1'].append([msg['Text'][4:], (itchat.search_friends(userName=msg['FromUserName']))["NickName"]])
        save_data("微信流水账登记.xls", data)
        return msg['Text']

itchat.auto_login(hotReload=True)
# 绑定消息响应事件后，让itchat运行起来，监听消息
itchat.run()