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

@bot.register()
def auto_reply(msg):
    if isinstance(msg.chat,Group):
        sender = msg.sender
        if (msg.type == 'Text'):
            message = {'type':msg.type,'text':msg.text,'file_path':''}
            data = {'sender_puid':sender.puid,'member_puid':msg.member.puid,'message' : message}
            res = requests.post('http://localhost:3000/wechat',json = data)
            res_data = json.loads(res.text)
            if (res_data['type']=='Text'):
                sender.send(res_data['info'])
    else:
        sender = msg.sender
        if (msg.type == 'Friends'):
            sender = bot.accept_friend(msg.card)
            message = {'type':msg.type,'text':msg.text,'file_path':''}
            data = {'sender_puid':sender.puid,'member_puid':'','message' : message}
            res = requests.post('http://localhost:3000/wechat',json = data)
            res_data = json.loads(res.text)
            sender.send(res_data['info'])      
        if (msg.type == 'Text'):
            message = {'type':msg.type,'text':msg.text,'file_path':''}
            data = {'sender_puid':sender.puid,'member_puid':'','message' : message}
            res = requests.post('http://localhost:3000/wechat',json = data)
            res_data = json.loads(res.text)
            if (res_data['type']=='add_member'):
                gs =  bot.groups().search(res_data['info'])
                if len(gs) == 0:
#                    base_users = users.friends()
#                    g = bot.create_group(base_users[len(base_users)-2]+[sender], topic=res_data['info'])
                    wy = bot.friends().search('文洋')[0]
                    g = bot.create_group([wy,sender], topic=res_data['info'])
                    g.send('Welcome! 欢迎 {}加入我们'.format(sender.name))
                if len(gs) > 0:
                    g = gs[0]
                    if sender not in g:
                        g.add_members(sender,'Welcome!')
                        g.send('Welcome! 欢迎 {}加入我们'.format(sender.name))
            if (res_data['type']=='Text'):
                sender.send(res_data['info'])
    print('3')
embed()

