import itchat
from pyexcel_xls import get_data
from pyexcel_xls import save_data

print('库存试题数：', len(get_data(r"C:/shaunpy/试题.xls")['试题']) - 1)
print('当前题目编号：', get_data(r"C:/shaunpy/试题.xls")['试题'][0][2])


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    data = get_data(r"C:/shaunpy/试题.xls")
    if msg['Text'] == '开始答题':
        return data['试题'][data['试题'][0][2]][0]
    elif msg['Text'] == str(data['试题'][data['试题'][0][2]][1]) or msg['Text'] == str.lower(
            data['试题'][data['试题'][0][2]][1]):
        if data['试题'][0][2] < len(data['试题']) - 1:
            data['试题'][0][2] = data['试题'][0][2] + 1
            save_data("试题.xls", data)
            return '答对了~答案是：' + data['试题'][data['试题'][0][2] - 1][1] + '\n请听下一题：' + data['试题'][data['试题'][0][2]][0]
        else:
            flag = data['试题'][0][2]
            data['试题'][0][2] = 1
            save_data("试题.xls", data)
            return '答对了~答案是：' + data['试题'][flag][1] + '\n已完成所有题目，恭喜~！\n题目已重置。\n请听下一题：' + data['试题'][data['试题'][0][2]][0]
    elif msg['Text'] in ('a', 'b', 'c', 'd', 'A', 'B', 'C', 'D') and msg['Text'] != str(
            data['试题'][data['试题'][0][2]][1]) and msg['Text'] != str.lower(data['试题'][data['试题'][0][2]][1]):
        save_data("试题.xls", data)
        return '答案不是' + msg['Text'] + '哦，再想想~'


itchat.auto_login(hotReload=True)
itchat.run()
