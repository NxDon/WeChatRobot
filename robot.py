#!/usr/bin/python3
import requests
from wxpy import *
import json
import logging

logging.basicConfig(level=logging.INFO)

# 减少网络层日志的干扰
for m in 'requests', 'urllib3':
    logging.getLogger(m).setLevel(logging.WARNING)

bot = Bot(cache_path=True)

# 开启 puid 获取功能，指定 puid 映射数据的保存路径
bot.enable_puid('wxpy_puid.pkl')


# 在群中回复用户文本消息　
@bot.register(Group, TEXT)
def auto_reply_text_in_groups(msg):
    sender = msg.sender
    message = {'type': msg.type, 'text': msg.text, 'file_path': ''}
    data = {'sender_puid': sender.puid, 'member_puid': msg.member.puid, 'message': message}
    res = requests.post('http://localhost:3000/wechat', json=data)
    res_data = json.loads(res.text)
    if (res_data['type'] == 'Text'):
        sender.send(res_data['info'])


# 机器人自动接受好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    sender = bot.accept_friend(msg.card)
    message = {'type': msg.type, 'text': msg.text, 'file_path': ''}
    data = {'sender_puid': sender.puid, 'member_puid': '', 'message': message}
    res = requests.post('http://localhost:3000/wechat', json=data)
    res_data = json.loads(res.text)
    if (res_data['type'] == 'Text'):
        sender.send(res_data['info'])

    # 私聊回复用户文本消息


@bot.register(Friend, TEXT)
def auto_reply_text_to_firends(msg):
    sender = msg.sender
    message = {'type': msg.type, 'text': msg.text, 'file_path': ''}
    data = {'sender_puid': sender.puid, 'member_puid': '', 'message': message}
    res = requests.post('http://localhost:3000/wechat', json=data)
    res_data = json.loads(res.text)
    if (res_data['type'] == 'Text'):
        sender.send(res_data['info'])
    if (res_data['type']=='add_member'):
        gs =  bot.groups().search(res_data['info'])
        sender.send('信息录入完毕，加群成功！')
        if len(gs) == 0:
            wy = bot.friends().search('文洋')[0]
            g = bot.create_group([wy, sender], topic=res_data['info'])
            g.send('Welcome! 欢迎 {}加入我们'.format(sender.name))
        if len(gs) > 0:
            g = gs[0]
            if sender not in g:
                g.add_members(sender, 'Welcome!')
                g.send('Welcome! 欢迎 {}加入我们'.format(sender.name))


embed()
