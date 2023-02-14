#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Gypsi的代码，Frag的心血。珍爱生命，远离抄袭。

import os  # 引入模块
import sys
import time
import XChat
import random
import _thread
import schedule

Admin = ["Frag", "DQJL68"]  # 设置Admin权限

CNL = ["restart", "addOP", "delOP", "ban", "bomb", "offline", "kick", "dumb", "help",
       "listOP"]  # 设置CommandNameList,指令名称列表。

CDL = ["重启Gypsi机器人", "添加协管权限识别码", "删除协管权限识别码",  # 设置CommandDetailList,指令详情列表。
       "伪封禁某位用户的识别码/名称", "轰炸某人", "下线某位用户", "踢出某位用户",
       "禁言某位用户", "查看指令帮助，有二级帮助", "协管列表"]

CUL = ["~restart", "~addOP <被添加者的==识别码==>", "~delOP <被删除者的==识别码==>",  # 设置CommandUsingList,指令使用方法列表。
       "~ban nick/trip add/del/list nick/trip(如使用list参数则不需要此条)",
       "~bomb <被轰炸者名字> <正整数>", "~offline (user)", "~kick (user)",
       "~dumb (user) (time)", "~help <指令名称（可选）>", "~listOP"]

ads = ["FragDev开发组招人啦!要求:技术上掌握基础python代码。无过高要求！ 欢迎前往 ?FragDev 了解详情。",  # 设置ads友情链接，用于宣传。
       "DCITYTEAM招人啦！要求:无过高要求！ 欢迎询问 灯确界L 了解详情。"]

OPlist = []  # 留空OPlist，下文在文件中读取后添加。
namefakeban = []  # 留空名称段伪封禁列表
tripfakeban = []  # 留空识别码伪封禁列表
Modlist = ["Outlier", "Frag", "stone", "Admin", "Y8WQ93", "cccccc", "iceice", "Win105",  # 设置管理员列表。
           "azazaz", "WQsbkl", "noip", "wuhu⭐", "orange", "YonHen", "5jbXdS", "yang"]

readme = """.                                                                                      #设置readme，给新人发送。
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


def reload():  # 设置reload函数，重新读取文件中的字符。
    OPlist.clear()
    with open('TrustedUsers.txt', encoding='utf-8') as OPget:
        line1 = OPget.readlines()
        for line in line1:
            OPlist.append(line.strip('\n'))
        OPget.close()

    namefakeban.clear()
    with open('bannedname.txt', encoding='utf-8') as BN:
        line2 = BN.readlines()
        for line in line2:
            namefakeban.append(line.strip('\n'))
        BN.close()

    tripfakeban.clear()
    with open('bannedtrip.txt', encoding='utf-8') as BT:
        line3 = BT.readlines()
        for line in line3:
            tripfakeban.append(line.strip('\n'))
        BT.close()


def message_got(message, sender, trip):  # 消息接收函数，当接收到消息会执行函数下的代码。
    # 下文的私信接收函数、用户加入/退出/错误报告函数均相同。

    if message.startswith("~bomb"):  # 轰炸指令判断，下文startswith判断均相同。
        if trip in OPlist:  # 判断用户是否符合权限，下文if trip in均相同。
            try:
                list2 = message.split()  # 将字符串切片，下文message.split()均相同。
                BombNumber = int(list2[2])  # 设定轰炸次数。
                for SpareInt in range(BombNumber):
                    xc.send_to(list2[1], "@{who} bomb!{bomb}".format(who=list2[1], bomb=SpareInt))  # 私信轰炸。
                    time.sleep(0.114514)
                time.sleep(2)
                xc.send_to(sender, "轰炸完成！")  # 执行后的反馈，下文的send_message或xc.send_to均相同。
            except IndexError:
                xc.send_to(sender, "缺少参数！")  # 缺少了参数，导致抛出IndexError.
            except ValueError:
                xc.send_to(sender, "您输入的数字不是正整数！")  # 数字不正确，导致抛出ValueError.
        else:
            xc.send_message("抱歉，您的权限无法执行此指令！")  # 不符合权限。

    if message.startswith("~help"):
        try:
            list3 = message.split()
            if list3[1] in CNL and message[6:] in CNL:  # 必须设置and，否则~help ban与~help ban10输出相同。
                CommandAll = CNL.index(list3[1])
                xc.send_to(sender, '''.                                                   #发送指令对应的help。
## 指令：{name}
|指令|{name}|
|-|-|
|作用|{detail}|
使用方法：输入{using}'''.format(name=CNL[CommandAll], detail=CDL[CommandAll], using=CUL[CommandAll]))
            else:  # 查询了错误的命令。
                xc.send_message("未知命令。")

        except IndexError:  # 没有设置查询的指令，导致抛出IndexError,此时需要发送全部的指令列表。
            xc.send_to(sender, ''' .
|等级|指令|
|-|-|
|Admin|\~restart|
|Mod|\~addOP,\~delOP,\~ban|
|OP|~bomb,\~offline,\~kick,\~dumb|
|Users|\~help,\~listOP|
FragBot小提示：1. FragDev 开发组招人啦！要求:技术上掌握基础python代码。无过高要求！ 欢迎前往 ?FragDev 了解详情。       #别问，问就是硬广
2.DCITYTEAM招人啦！要求:无过高要求！ 欢迎询问 灯确界L 了解详情。
3. 这个bot由灯确界托管，所以灯确界是联合作者！awa''')

    if message.startswith("~addOP"):
        list10 = message.split()
        if trip in Modlist:
            try:
                if list10[1] in OPlist:  # 如果已经含有，那么不再添加。
                    xc.send_message("该用户已经是协管啦。")
                else:
                    addOP = open('using/TrustedUsers.txt', mode='a+', encoding='UTF-8')  # 打开文件，写入目标的识别码。记得关闭。
                    addOP.write(list10[1] + "\n")
                    addOP.close()
                    xc.send_message("添加成功！识别码：{}".format(list10[1]))

                    reload()

            except IndexError:  # 没有设置识别码，导致抛出IndexError。
                xc.send_message("添加失败！")
        else:
            xc.send_message("抱歉，您的权限无法执行此指令！")

    if message.startswith("~delOP"):
        list11 = message.split()
        if trip in Modlist:
            try:  # 把原有的协管识别码替换成空，目前随意替换，即使识别码不存在于里面。
                delOP = open('using/TrustedUsers.txt', 'r+', encoding='UTF-8')
                OPget = delOP.readlines()
                delOP = open('using/TrustedUsers.txt', 'w+', encoding='UTF-8')
                for i in OPget:
                    delOP.write(i.replace(list11[1] + "\n", ""))

                reload()  # 重新加载，否则不会生效。下文的reload()均相同。

                xc.send_message("删除成功！识别码：{}".format(list11[1]))
            except IndexError:
                xc.send_message("删除失败！")
        else:
            xc.send_message("抱歉，您的权限无法执行此指令！")

    if message.startswith("~restart"):
        if trip in Admin:
            xc.send_message("即将重启...")
            time.sleep(1)
            restart = sys.executable  # 将自身重启。
            os.execl(restart, restart, *sys.argv)
        else:
            xc.send_message("抱歉，您的权限无法执行此指令！")

    if message.startswith("~listOP"):
        a = ",".join(OPlist)  # 把逗号插入于每一个列表元素中间。
        xc.send_message("OP列表：" + a)

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
                        xc.send_message("名称段伪封禁列表：" + hm)

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
                        xc.send_message("识别码伪封禁列表：" + hm)

            except IndexError:
                xc.send_message("参数错误！")
        else:
            xc.send_message("拒绝执行！")


def user_join(nick, trip):
    time.sleep(1)
    xc.send_to(nick, "欢迎来到XChat聊天室，祝您在这里聊天愉快~")  # 发送欢迎语。

    for i in range(namefakeban.index(namefakeban[-1]) + 1):  # 与名称段伪封禁列表一一检查，如果有一项匹配就踢出此用户。
        # 下文识别码伪封禁列表也类似。
        if namefakeban[i] in nick:
            xc.send_message("/kick {user} banned".format(user=nick))

    for i in range(tripfakeban.index(tripfakeban[-1]) + 1):
        if tripfakeban[i] == trip:
            xc.send_message("/kick {user} banned".format(user=nick))


def user_leave(nick):
    if nick in ["fish", "Fish", "MelonFish", "idle_fish", "fish_idle"]:  # 如果离开的用户是fish，就发出凄厉的叫声（划去
        xc.send_message("F—I—S—H——")


def whisper_got(message, nick, trip):
    xc.send_message("别私聊我，" + nick + "。")  # 不开放私聊，并把私聊我的用户公开处刑。


def kill_errors(info):
    if info != "你点击了太多次！":
        xc.send_message("Gypsi出错啦！详细信息：" + info)  # 发出错误信息，频率限制除外。
        # 因为报出频率限制错误时，继续发送消息会会加剧限制程度。


def lockroom():  # 锁房函数1，负责上锁。由schedule调用。锁房函数2类似。
    xc.send_message("/lockroom")
    xc.send_message("该锁房啦\~ 大家晚安\~")


def unlockroom():  # 锁房函数2，负责解锁。
    xc.send_message("/unlockroom")
    xc.send_message("该解锁啦\~ 各位早上好啊\~")


def adsending():  # 发送随机的广告，由schedule调用。
    xc.send_message(random.choice(ads))


schedule.every().day.at("07:30").do(unlockroom)
schedule.every().day.at("22:30").do(lockroom)
schedule.every(45).minutes.do(adsending)


def looping():  # 定义一个检测schedule的函数，由下文启动新线程调用，否则会阻塞。
    while True:
        schedule.run_pending()


_thread.start_new_thread(looping, ())  # 启动looping函数。

xc = XChat.XChat("DQJLSTOKEN", "xq102210", "Gypsi", "Shimano105YYDS")  # 提供4个参数分别是机器人的token、聊天室名称、昵称、密码。
xc.message_function += [message_got]
xc.join_function += [user_join]
xc.leave_function += [user_leave]
xc.whisper_function += [whisper_got]
xc.error_function += [kill_errors]
time.sleep(0.5)
xc.send_message("全新Gypsi运行成功！输入`~help`查看帮助。")  # 发送启动语。
print("Start!")
reload()
xc.run(False)  # 死循环，作用是持续接收消息。
