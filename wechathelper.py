import time
import itchat

# 确认目前系统时间是否正常
print('\n目前系统时间为：', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 登录itchat
itchat.auto_login(hotReload=True)

# 获取测试群的id
ceshiqun = itchat.search_chatrooms(name=u'测试群')[0]['UserName']

# 获取当日日常工作和值班表
ykmingdan = ('刘哲、杜璞', '李晓燕、潘津', '柳备、邵帅', '郭雷、周海敏',
             '刘立军、冀平', '李捍华、李肖肖', '李海洋、梁海腾')
ykrichang = ('下班前完成MIS缺陷录入、反违章检查问题填报、上周异常事件台账登记',
             '中午前完成周维护计划填报', '下班前完成周常巡检', '中午前完成缺陷分析', '无', '无', '无')
ykzhiban = '今日值班人员（默认）：' + ykmingdan[(int(time.time() / 86400) % 8) - 1]
ykgongzuo = '今日日常工作：' + ykrichang[int(time.strftime("%w")) - 1]

while True:
    # 8:00发送当日日常工作
    if time.strftime("%H%M", time.localtime()) == "0800":
        itchat.send(ykgongzuo, toUserName=ceshiqun)
        print(ykgongzuo)
        time.sleep(61)

    # 月末提醒填报安全审核
    elif time.strftime("%H%M", time.localtime()) == "0801" \
            and int(time.strftime("%d", time.localtime())) in {27, 28, 29, 30, 31}:
        itchat.send('温馨提示：临近月末，请填报安全审核。', toUserName=ceshiqun)
        print('温馨提示：临近月末，请填报安全审核。')
        time.sleep(61)

    # 周一提醒1:30召开班会
    elif time.strftime("%H%M", time.localtime()) == "1310" and int(time.strftime("%w")) == 1:
        itchat.send('温馨提示：今日周一，1:30召开班级会。', toUserName=ceshiqun)
        print('温馨提示：今日周一，1:30召开班级会。')
        time.sleep(61)

    # 下班提醒工作收尾和值班
    elif time.strftime("%H%M", time.localtime()) == "1600":
        itchat.send('温馨提示：临近下班，请确认本日工作台账已登记，并记录点检日志。', toUserName=ceshiqun)
        print('温馨提示：临近下班，请确认本日工作台账已登记，并记录点检日志。')
        itchat.send(ykzhiban, toUserName=ceshiqun)
        print(ykzhiban)
        time.sleep(61)
