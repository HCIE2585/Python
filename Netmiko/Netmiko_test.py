#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import time
import sys
import json
from netmiko import ConnectHandler                          # 引入netmiko的核心对象
import pprint
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
device = {
        'device_type': 'cisco_ios',
        'host': '192.168.123.30',
        'username': 'cisco',
        'password': 'cisco',
 }
# 定义一个字典，包含设备类型（netmiko支持的设备类型很多），host（ip）,username,password ,
try:
    connect = ConnectHandler(**device)                          # 登陆设备，可以直接输入需要登陆的设备参数
    print("已经成功登陆交换机:" + device['host'])
    print("开始执行命令")
    output = connect.send_command('show version',use_genie=True)               # send_command()：只支持向设备发送一条命令，通常是show/display/save之类的查询、排错、保存命令
    output1 = connect.send_command('show ip interface brief',use_genie=True)
    # pprint(output1)
    log = open(device['host'] + '-' + LogTime + '.txt', 'w')
    log.write(json.dumps(output,indent=2)+ '\n' + json.dumps(output1,indent=2))
    log.close()
except:
    print("程序5s后退出")


time.sleep(1)