#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import time
import sys
from netmiko import ConnectHandler     # 引入netmiko的核心对象
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
device = {
        'device_type': 'hp_comware',
        'host': '10.93.2.62',
        'username': 'banner',
        'password': 'Ops1@12345',
 }
                                        # 定义一个字典，包含设备类型（netmiko支持的设备类型很多），host（ip）,username,password ,
connect = ConnectHandler(**device)      # 登陆设备，可以直接输入需要登陆的设备参数
print("已经成功登陆交换机:" + device['host'])
print("开始执行命令")
output = connect.send_command('dis cur')  # send_command()：只支持向设备发送一条命令，通常是show/display/save之类的查询、排错、保存命令
log = open(device['host'] + '-' + LogTime + '.txt', 'w')
log.write(output)
log.close()
print("程序5s后退出")
time.sleep(1)