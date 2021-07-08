#!/usr/bin/python
# -*- coding:gb2312 -*-
#import tab
import time         #导入系统时间
import subprocess
time = float (time.time())
print('Start ICMP Test! Please wait a monment!')
ips = open('IP_List.txt', 'r')                   # 只读方式打开文本文件ips
ip_True = open('IP_True.txt', 'w')               # 创建文本文件IP_True.txt，w 表示只写，记录ping测成功的IP
ip_False = open('IP_False.txt', 'w')             # 创建文本文件IP_False.txt，w 表示只写，记录ping测失败的IP
count_True,count_False=0,0
for ip in ips.readlines():
        ip = ip.strip()
        print('Start Ping %s' % ip)
        ping_result = subprocess.call(['ping','-c','3',ip])
        if ping_result == 0:
                print('Ping %s is OK' % ip)
                ip_True.write(ip + '\n')
                count_True += 1
        else:
                print('Ping %s is Fail' % ip)
                ip_False.write(ip + '\n')
                count_False += 1
ip_True.close()
ip_False.close()
ips.close()
print ("The Numerber of Sucessful Tests:",count_True)
print ("The Numerber of Failed Tests:",count_False)


