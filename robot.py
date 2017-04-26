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
enable_puid('wxpy_puid.pkl')

@bot.register()
def auto_reply(msg):
    print(msg.chat)
    print(msg)
    if isinstance(msg.chat,Group):
        print('2')
        sender = msg.sender
        if (msg.type == 'Text'):
            message = {'type':msg.type,'text':msg.text,'file_path':''}
            data = {'sender_puid':sender.puid,'member_puid':msg.member.puid,'message' : message}
            res = requests.post('http://localhost:3000/wechat',json = data)
            res_data = json.loads(res.text)
            if (res_data['type']=='Text'):
                sender.send(res_data['info'])
    else:
        print('1')
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
#                g =  bot.groups().search(puid=res_data['info'])[0]
#                g =  bot.groups().search(g.name)[0]
                g =  bot.groups().search('测试')[0]
                if sender not in g:
                    g.add_members(sender,'Welcome!')
            if (res_data['type']=='Text'):
                sender.send(res_data['info'])
   
    print('3')
embed()

