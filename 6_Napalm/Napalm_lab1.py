#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import time
import sys
from napalm import get_network_driver
import json
driver = get_network_driver('huawei_vrp')
device = driver(hostname='10.93.0.15', username='banner', password='Ops1@12345')
device.open()
get_facts = device.get_facts()
print(json.dumps(get_facts,indent=2))
log = open('1.txt','w')
log.write(json.dumps(get_facts,indent=2))
log.close()
send_command = device.cli(['dis ver'])
log2 = open('2.txt','w')
log2.write(json.dumps(send_command,indent=2))
log2.close()
