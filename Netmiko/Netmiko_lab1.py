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
        'host': '10.93.1.62',
        'username': 'banner',
        'password': 'Ops1@12345',
 }
connect = ConnectHandler(**fw)
output = connect.send_command('dis ip routing-table ',use_textfsm=True)
pprint(output)
print (json.dumps(output, indent=2))
log = open(fw['host'] + '-' + LogTime + '.txt', 'w')
# for output_dict in output:
    # for key, value in output.items
    #     log.write(str(value))
# for content in output:
#     log.write(content)
log.write(json.dumps(output, indent=2))
for item in output:
    print(item["network"])
print (len(output))
log.close()


xmr.f2pool.com
task4.wyptwilight.cn
dd.avrenren.com
donate.v2.xmrig.com
pop.consultinginc.ru
upgrades.ddns.net
2xxxxxx.com
jincc.cc
bj2.haoxiw.com
emergency.googel-dns.com