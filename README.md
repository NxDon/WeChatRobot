##微信自动加群机器人

# robot-if-else
#### 启动数据库  mongodb 
[https://docs.mongodb.com/manual/installation/](https://docs.mongodb.com/manual/installation/)
#### 运行后台程序 robot-student-management

```
➜  robot-if-else git:(master) git clone https://github.com/Aym-fuhong/robot-student-management.git
➜  robot-if-else git:(master) ✗ cd robot-student-management 
➜  robot-student-management git:(master) npm start

> mongoose01@1.0.0 start /home/zhyingjia/PythonProjects/robot-if-else/robot-student-management
> nodemon --exec npm run babel-node -- app.js
> mongoose01@1.0.0 babel-node /home/zhyingjia/PythonProjects/robot-if-else/robot-student-management
> babel-node "app.js"

server started at http://localhost:3000
connect success

```
#### 运行微信程序 robot.py
 - 安装开发分支

```
pip3 install -U git+https://github.com/youfou/wxpy.git@develop
```
 - 运行程序

```
➜  robot-if-else git:(master) ✗ ./robot.py 

...微信二维码　（扫码登录）
```
