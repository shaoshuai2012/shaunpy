#!/usr/bin/python
# -*- coding: utf-8 -*-

import platform
import itchat
import sys
from pyexcel_xls import get_data
from pyexcel_xls import save_data

if platform.system() == 'Darwin':  # Mac环境下题库文件路径
    location = r"/Users/ShaoShuai/Desktop/shaunpy/试题.xls"
elif platform.system() == 'Windows':  # Windows环境下题库文件路径
    location = r"C:/shaunpy/试题.xls"
else:
    print('系统环境未知，请重新设置文件路径！')
    sys.exit(0)

# 输出当前试题库情况
print('库存试题数：', len(get_data(location)['试题']) - 1, '\n当前题目编号：', get_data(location)['试题'][0][2])
score = {}


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    data = get_data(location)  # 读取试题文件
    ans = data['试题'][data['试题'][0][2]][1]
    name = msg['ActualNickName']
    if msg['Text'] == '开始答题':  # 开始答题时，返回当前序号对应题目
        return '请听题：\n' + data['试题'][data['试题'][0][2]][0]
    elif msg['Text'] == '查看成绩':  # 查看成绩时，输出所有姓名对应成绩
        paihang = sorted(score.items(), key=lambda d: d[1], reverse=True)  # 对成绩排序
        chengji = ''
        for i in range(len(paihang)):
            chengji = chengji + '第' + str(i+1) + '名：' + paihang[i][0] + '  成绩：' + str(paihang[i][1]) + '分\n'
        return chengji
    elif msg['Text'] in [str(ans), str.lower(ans)]:  # 如果答对了
        if name in score.keys():  # 如果名单列表里已有，为对应名字加分
            score[name] = score[name] + 1
        else:  # 如果名单列表里没有，增加名字，并给分
            score[name] = 1
        if data['试题'][0][2] < len(data['试题']) - 1:  # 如果答对且还有题目，发送答案和下一题题目
            data['试题'][0][2] = data['试题'][0][2] + 1
            save_data("试题.xls", data)
            return '答对了~答案是：' + data['试题'][data['试题'][0][2] - 1][1] + \
                   '\n\n请听下一题：\n' + data['试题'][data['试题'][0][2]][0]
        else:  # 如果答对且没有题目了，发送答案并从第一题开始
            flag = data['试题'][0][2]
            data['试题'][0][2] = 1
            save_data("试题.xls", data)
            return '答对了~答案是：' + data['试题'][flag][1] + \
                   '\n\n已完成所有题目，恭喜~！\n题目已重置。\n\n请听第一题：\n' + data['试题'][1][0]
    elif msg['Text'] in ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D'] and \
            msg['Text'] not in [str(ans), str.lower(ans)]:  # 如果答错了，提示错误
        if name in score.keys():  # 如果名单列表里已有，为对应名字扣分
            score[name] = score[name] - 1
        else:  # 如果名单列表里没有，增加名字，并扣分
            score[name] = -1
        save_data("试题.xls", data)
        return '答案不是' + msg['Text'] + '哦，再想想~'
    else:
        pass


itchat.auto_login(hotReload=True)  # 登录itchat并运行
itchat.run()
