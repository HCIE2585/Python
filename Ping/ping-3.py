#!/usr/bin/python
# -*- coding:gb2312 -*-
import time         #导入系统时间
from pythonping import ping
import os
time = float (time.time())
print('Start ICMP Test! Please wait a monment!')
ips = open('IP_List.txt', 'r')                   # 只读方式打开文本文件ips
ip_True = open('IP_True.txt', 'w')               # 创建文本文件IP_True.txt，w 表示只写，记录ping测成功的IP
ip_False = open('IP_False.txt', 'w')             # 创建文本文件IP_False.txt，w 表示只写，记录ping测失败的IP
count_True,count_False=0,0
for ip_address in ips.readlines():
        # for ip4 in last_octet:
        host = ip_address.strip()
        print('Start Ping %s' % host)
        result = ping(host)
        if 'Reply' in str(result):
                print('Ping %s is OK' % host)
                ip_True.write(host + '\n')
                count_True += 1
        else:
                print('Ping %s is Fail' % host)
                ip_False.write(host + '\n')
                count_False += 1
ip_True.close()
ip_False.close()
ips.close()
print ("The Numerber of Sucessful Tests:",count_True)
print ("The Numerber of Failed Tests:",count_False)


