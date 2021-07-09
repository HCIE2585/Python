#!/usr/bin/python
# -*- coding:gb2312 -*-
import time  # 导入系统时间
from pythonping import ping
time = float(time.time())
print('Start ICMP Test! Please wait a monment!')
ips = open('IP_List.txt', 'r')
ip_True = open('Reachable.txt', 'w')
ip_False = open('Unreachable.txt', 'w')
count_True, count_False = 0, 0
for ip_address in ips.readlines():
    host = ip_address.strip()
    print('Start Ping %s' % host)
    result = ping(host)
    print(result)
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
print("The Numerber of Sucessful Tests:", count_True)
print("The Numerber of Failed Tests:", count_False)
