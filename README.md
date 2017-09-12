
## 微信自动加群机器人

  配合 [robot-student-management](https://github.com/NxDon/wxRobot-manager.git)食用，实现微信自动拉人加群，录入个人信息等功能。

#### 启动数据库  mongodb
[https://docs.mongodb.com/manual/installation/](https://docs.mongodb.com/manual/installation/)

#### 运行后台程序 robot-student-management
- 安装依赖项并启动服务器
```
    cd robot-student-management
    npm install
    npm start
```
#### 运行微信程序 robot.py

 - 安装开发分支

```
    pip3 install -U git+https://github.com/youfou/wxpy.git@develop
```
 - 运行程序

```
  python3 robot.py

  微信二维码　（扫码登录）
```
