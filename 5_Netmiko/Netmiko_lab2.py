#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import time
import sys
from netmiko import ConnectHandler
from pprint import pprint
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
fw = {
        'device_type': 'hp_comware',
        'host': '10.93.2.62',
        'username': 'banner',
        'password': 'Ops1@12345',
 }
commands= ['interface lo100','des test1','inter lo101','des test2']
with ConnectHandler(**fw) as connect:                               # 用了context manager（上下文管理器，也就是with语句）来调用ConnetHandler，它的好处是可以在脚本运行完毕后自动帮助我们关闭SSH会话
    print("已经成功登陆交换机:" + fw['host'])
    print("开始执行命令")
    output1 = connect.send_command('dis ip int brief | in "up"')    # send_command()：只支持向设备发送一条命令，通常是show/display/save之类的查询、排错、保存命令
    print(output1)
    output2 = connect.send_config_set(commands)                     # send_conifg_set():向设备发送一条或多条配置命令,一般配合列表使用。会自动添加 config t / system等命令
    print(output2)
    output3 = connect.send_config_from_file('h3c_cmd_lab2.txt')     # send_config_from_file():读预定义好的配置文件的内容帮助我们完成配置
    print(output3)
    output4 = connect.save_config()                                 # save_config():保存配置，思科的wr，华为save等
    print(output4)
log = open(fw['host'] + '-' + LogTime + '.txt', 'w')
log.write(output1+output2+output3+output4)
log.close()