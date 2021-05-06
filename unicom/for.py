#!/usr/bin/python
#-*- coding: utf-8 -*-
import re
import telnetlib
import time
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
time.sleep(1)
for line in open("access_list.txt"):
	print(line)
	time.sleep(2)
        host = line.replace('\n', '')
        print("Start telnet", host)
