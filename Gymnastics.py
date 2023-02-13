# Gypsi的代码，Frag的心血。珍爱生命，远离抄袭。
#-*- coding = utf-8 -*-

import XChat  # 引入模块
import time
import sys
import os
import random
import schedule
import _thread

Admin = ["Frag","DQJL68"]

CNL = ["restart","addOP","delOP","ban","bomb","offline","kick","dumb","help","listOP"]

CDL = ["重启Gypsi机器人","添加协管权限识别码","删除协管权限识别码",
       "伪封禁某位用户的识别码/名称","轰炸某人","下线某位用户","踢出某位用户",
        "禁言某位用户","查看指令帮助，有二级帮助","协管列表"]

CUL = ["~restart","~addOP <被添加者的==识别码==>","~delOP <被删除者的==识别码==>",
       "~ban nick/trip add/del/list nick/trip(如使用list参数则不需要此条)",
       "~bomb <被轰炸者名字> <正整数>","~offline (user)","~kick (user)",
       "~dumb (user) (time)", "~help <指令名称（可选）>","~listOP"]

ads = ["FragDev开发组招人啦!要求:技术上掌握基础python代码。无过高要求！ 欢迎前往 ?FragDev 了解详情。",
       "DCITYTEAM招人啦！要求:无过高要求！ 欢迎询问 灯确界L 了解详情。"]

OPlist = []
namefakeban = []
tripfakeban = []
Modlist = ["Outlier","Frag","stone","Admin","Y8WQ93","cccccc","iceice","Win105",
           "azazaz","WQsbkl","noip","wuhu⭐","orange","YonHen","5jbXdS","yang"]

readme = """.
## 嘿陌生人，欢迎来到XChat！
这是一个小型且匿名的聊天室，里面的人们都很友善哦
_____
下面是几个小小的提示：
### 密码，管理和识别码
设置密码的方式很简单，在输入昵称一栏输入以下格式：`昵称#密码`
比如`iloveXC#123456` 在头像左方就会出现识别码`pisqfw`
==请注意：一些简单的密码会和他人重复且容易被猜出，请设置复杂密码且牢记。==
如果是管理的话前方会有一个“★”，用来标识此人为管理或站长。
注：一些识别码为站长手动替换而成，例如站长的识别码为`Admin`
### 昵称颜色
你可以手动修改自己的昵称颜色，请使用16进制颜色。
例如`/color 00ff00`会让自己的颜色改成绿色，如果需要回归原本颜色，请输入`/color none`即可。
以主题atelier-dune为例，站长颜色默认是红色，管理员是青色，用户是蓝色。
### 设定头像
头像是XChat的一大特色，你可以将图片上传到[Postimages.org](https://postimages.org)或[imgtu](https://imgtu.com)复制直接图片链接后，在侧边栏选择”设置头像“粘贴链接即可。
注：直接图片链接多为webp，jpeg；jpg和png结尾，请确认后键入。
### 发送图片
和上一个一样，需要把图片上传到图床后选择”Markdown“开头的链接粘贴发送即可
这种链接以`![]`开头或`[![]`开头。
### 机器人
机器人在进入时会提示来自“某个机房”。 ==注：有些人使用不同的客户端连接时也会提示，请仔细辨别！==
机器人昵称一般末尾会有“Bot”等字样
_____
同时，在这里发言请遵守以下规则：
- 严禁发送辱骂国家或线圈团队等消息
- 严禁在公屏讨论色情淫秽信息
- 进制发送过多无意义信息
- 可以发送广告，但不能发送包含辱骂、赌博，以及其他聊天室的信息，且一小时打广告需低于3次
- 发送较长消息时需要提示，比如：长警
_____
最后感谢你加入XChat聊天室！
###### 2023 XQ Team --- 2019-2023 Windows10555 Team --- 2022-2023 DCITYTEAM"""

def reload():
    OPlist.clear()
    with open('using/TrustedUsers.txt', encoding='utf-8') as OPget:
        line1 = OPget.readlines()
        for line in line1:
            OPlist.append(line.strip('\n'))
        OPget.close()

    namefakeban.clear()
    with open('ban/bannedname.txt', encoding='utf-8') as BN:
        line2 = BN.readlines()
        for line in line2:
            namefakeban.append(line.strip('\n'))
        BN.close()

    tripfakeban.clear()
    with open('ban/bannedtrip.txt', encoding='utf-8') as BT:
        line3 = BT.readlines()
        for line in line3:
            tripfakeban.append(line.strip('\n'))
        BT.close()

def message_got(message, sender, trip):
    if message.startswith("~bomb"):
        if trip in OPlist:
            try:
                list2 = message.split()
                BombNumber = int(list2[2])
                for SpareInt in range(BombNumber):
                    xc.send_message("/w {who} @{who} bomb!{bomb}".format(who=list2[1], bomb=SpareInt))
                    time.sleep(0.114514)
            except IndexError:
                xc.send_to(sender,"缺少参数！".format(who=sender))
            except ValueError:
                xc.send_to(sender,"您输入的数字不是正整数！")
        else:
            xc.send_message("抱歉，您的权限无法执行此指令！")

    if message.startswith("~help"):
        try:
            list3 = message.split()
            if list3[1] in CNL and message[6:] in CNL:
                CommandAll = CNL.index(list3[1])
                xc.send_to(sender,'''.
## 指令：{name}
|指令|{name}|
|-|-|
|作用|{detail}|
使用方法：输入{using}'''.format(name=CNL[CommandAll], detail=CDL[CommandAll], using=CUL[CommandAll])
            else:
                xc.send_message("未知命令。")

        except IndexError:
            xc.send_to(sender,''' .
|等级|指令|
|-|-|
|Admin|\~restart|
|Mod|\~addOP,\~delOP,\~ban|
|OP|~bomb,\~offline,\~kick,\~dumb|
|Users|\~help,\~listOP|
FragBot小提示：1. FragDev 开发组招人啦！要求:技术上掌握基础python代码。无过高要求！ 欢迎前往 ?FragDev 了解详情。
2.DCITYTEAM招人啦！要求:无过高要求！ 欢迎询问 灯确界L 了解详情。
3. 这个bot由灯确界托管，所以灯确界是联合作者！awa''')

    if message.startswith("~addOP"):
        list10 = message.split()
        if trip in Modlist:
            try:
                if list10[1] in OPlist:
                    xc.send_message("添加失败！")
                else:
                    addOP = open('using/TrustedUsers.txt', mode='a+', encoding='UTF-8')
                    addOP.write(list10[1] + "\n")
                    addOP.close()
                    xc.send_message("添加成功！识别码：{}".format(list10[1]))

                    reload()

            except IndexError:
                xc.send_message("添加失败！")
        else:
            xc.send_message("抱歉，您的权限无法执行此指令！")

    if message.startswith("~delOP"):
        list11 = message.split()
        if trip in Modlist:
            try:
                delOP = open('using/TrustedUsers.txt', 'r+', encoding='UTF-8')
                OPget = delOP.readlines()
                delOP = open('using/TrustedUsers.txt', 'w+', encoding='UTF-8')
                for i in OPget:
                    delOP.write(i.replace(list11[1] + "\n", ""))

                reload()
                        
                xc.send_message("删除成功！识别码：{}".format(list11[1]))
            except IndexError:
                xc.send_message("删除失败！")
        else:
            xc.send_message("抱歉，您的权限无法执行此指令！")

    if message.startswith("~restart"):
        if trip in Admin:
            xc.send_message("即将重启...")
            time.sleep(1)
            restart = sys.executable
            os.execl(restart, restart, *sys.argv)
        else:
            xc.send_message("抱歉，您的权限无法执行此指令！")
        

    if message.startswith("~listOP"):
        a = ",".join(OPlist)
        xc.send_message("OP列表：" + a )

    if message.startswith("~offline"):
        list_offline = message.split()
        if trip in OPlist:
            try:
                xc.send_message("/offline {user}".format(user=list_offline[1]))
            except IndexError:
                xc.send_message("参数错误！")
        else:
            xc.send_message("抱歉，您的权限无法执行此指令！")

    if message.startswith("~kick"):
        list_kick = message.split()
        if trip in OPlist:
            try:
                xc.send_message("/kick {user}".format(user=list_kick[1]))
            except IndexError:
                xc.send_message("参数错误！")
        else:
            xc.send_message("抱歉，您的权限无法执行此指令！")

    if message.startswith("~dumb"):
        list_dumb = message.split()
        if trip in OPlist:
            try:
                if float(list_dumb[2]) > 5:
                    xc.send_message("为防止滥用，此命令单次最多禁言用户 5 分钟。")
                elif list_dumb[2] == "0":
                    xc.send_message("协管不可永久禁言用户。")
                else:
                    print(float(list_dumb[2]))
                    xc.send_message("/dumb {user} {time}".format(user=list_dumb[1], time=list_dumb[2]))
            except Exception:
                xc.send_message("参数错误！")
        else:
            xc.send_message("抱歉，您的权限无法执行此指令！")

    if message.startswith("~ban"):
        if trip in Modlist:
            try:
                list_fakeban = message.split()
                if list_fakeban[1] == "nick":

                    if list_fakeban[2] == "add":
                        banneduser = list_fakeban[3]
                        namefakeban.append(banneduser)
                        addban = open('ban/bannedname.txt', mode='a+', encoding='UTF-8')
                        addban.write(banneduser + "\n")
                        addban.close()
                        xc.send_message("操作成功！")

                    if list_fakeban[2] == "del":
                        banneduser = list_fakeban[3]
                        delban = open('ban/bannedname.txt', 'r+', encoding='UTF-8')
                        ban = delban.readlines()
                        delban = open('ban/bannedname.txt', 'w+', encoding='UTF-8')
                        for i in ban:
                            delban.write(i.replace(banneduser + "\n", ""))
                        xc.send_message("操作成功！")

                    if list_fakeban[2] == "list":
                        hm = ",".join(namefakeban)
                        xc.send_message("名称段伪封禁列表："+hm)

                if list_fakeban[1] == "trip":

                    if list_fakeban[2] == "add":
                        banneduser = list_fakeban[3]
                        tripfakeban.append(banneduser)
                        addban = open('ban/bannedtrip.txt', mode='a+', encoding='UTF-8')
                        addban.write(banneduser + "\n")
                        addban.close()
                        xc.send_message("操作成功！")

                    if list_fakeban[2] == "del":
                        banneduser = list_fakeban[3]
                        delban = open('ban/bannedtrip.txt', 'r+', encoding='UTF-8')
                        ban = delban.readlines()
                        delban = open('ban/bannedtrip.txt', 'w+', encoding='UTF-8')
                        for i in ban:
                            delban.write(i.replace(banneduser + "\n", ""))
                        xc.send_message("操作成功！")

                    if list_fakeban[2] == "list":
                        hm = ",".join(tripfakeban)
                        xc.send_message("识别码伪封禁列表："+hm)
                
            except IndexError:
                xc.send_message("参数错误！")
        else:
            xc.send_message("拒绝执行！")

def user_join(nick, trip):
    time.sleep(1)
    xc.send_to(nick,"欢迎来到XChat聊天室，祝您在这里聊天愉快~")

    for i in range(namefakeban.index(namefakeban[-1])+1):
        if namefakeban[i] in nick:
            xc.send_message("/kick {user} banned".format(user=nick))

    for i in range(tripfakeban.index(tripfakeban[-1])+1):
        if tripfakeban[i] == trip:
            xc.send_message("/kick {user} banned".format(user=nick))

def user_leave(nick):
    if nick in ["fish","Fish","MelonFish","idle_fish","fish_idle"]:
        xc.send_message("F—I—S—H——")
    
def whisper_got(message, nick, trip):
    xc.send_message("别私聊我，"+nick+"。")

def kill_errors(info):
    if info != "你点击了太多次！":
        xc.send_message("Gypsi出错啦！详细信息："+info)
    
def lockroom():
    xc.send_message("/lockroom")
    xc.send_message("该锁房啦\~ 大家晚安\~")

def unlockroom():
    xc.send_message("/unlockroom")
    xc.send_message("该解锁啦\~ 各位早上好啊\~")

def ads():
    xc.send_message(random.choice(ads))

schedule.every().day.at("07:30").do(unlockroom)
schedule.every().day.at("22:30").do(lockroom)
schedule.every(45).minutes.do(ads)

def looping():
    while True:
        schedule.run_pending()

_thread.start_new_thread(looping,())

xc = XChat.XChat("DQJLSTOKEN", "xq102210", "Gymdemocs", "Shimano105YYDS")
xc.message_function += [message_got]
xc.join_function += [user_join]  
xc.leave_function += [user_leave]
xc.whisper_function += [whisper_got] 
xc.error_function += [kill_errors]
time.sleep(0.5)
xc.send_message("全新Gypsi运行成功！输入`~help`查看帮助。")
print("Start!")
reload()
xc.run(False)
