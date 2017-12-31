import itchat

# 注册消息响应事件，消息类型为itchat.content.TEXT，即文本消息
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    # 返回同样的文本消息
    return msg['Text']

itchat.auto_login()
# 绑定消息响应事件后，让itchat运行起来，监听消息
itchat.run()