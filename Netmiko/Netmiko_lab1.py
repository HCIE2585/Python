#!/usr/bin/python
#-*- coding: utf-8 -*-
import re
import time
import sys
from netmiko import ConnectHandler
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
fw = {
        'device_type': 'hp_comware',
        'host': '10.93.1.62',
        'username': 'banner',
        'password': 'Ops1@12345',
 }
connect=ConnectHandler(**fw)
# config_commands=['screen-length disable','display cur']
output=connect.send_command('dis cur')
print(output)
log = open(fw['host'] + '-' + LogTime + '.txt', 'w')  # 定义个log文本文件，
log.write(output) # 把info信息写到log中，
log.close()  # 关闭log文件