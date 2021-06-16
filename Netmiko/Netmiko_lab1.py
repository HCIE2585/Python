#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import time
import sys
from netmiko import ConnectHandler
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
device = {
        'device_type': 'hp_comware',
        'host': '10.93.2.62',
        'username': 'banner',
        'password': 'Ops1@12345',
 }
connect = ConnectHandler(**device)
output = connect.send_command('dis cur')
log = open(device['host'] + '-' + LogTime + '.txt', 'w')
log.write(output)
log.close()
