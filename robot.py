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
#        if (msg.type  in ['Picture','Recording','Attachment','Video'] ):
#            print(msg.file_name)
#            file_path = './data/' + msg.file_name
#            print('1')
#            msg.get_file(file_path)
#            print('2')
#            message = {'type':msg.type,'text':msg.text,'file_path':file_path}
#            print('3')
#            data = {'sender_puid':sender.puid,'member_puid':'','message' : message}
#            print('4')
#            res = requests.post('http://localhost:3000/wechat',json = data)
#            print('5')
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

