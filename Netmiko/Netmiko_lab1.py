#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import time
import sys
import json
from netmiko import ConnectHandler
from pprint import pprint
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
fw = {
        'device_type': 'hp_comware',
        'host': '10.93.2.62',
        'username': 'banner',
        'password': 'Ops1@12345',
 }
connect = ConnectHandler(**fw)
output = connect.send_command('dis ip routing',use_textfsm=True)
pprint(output)
# print (json.dumps(output, indent=2))
log = open(fw['host'] + '-' + LogTime + '.txt', 'w')
# for output_dict in output:
    # for key, value in output.items
    #     log.write(str(value))
# for content in output:
#     log.write(content)
log.write(json.dumps(output, indent=2))
log.close()
for item in output:
     print(item["protocal"])
print (len(output))

