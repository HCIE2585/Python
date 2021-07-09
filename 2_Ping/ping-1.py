#!/usr/bin/python
# -*- coding:gb2312 -*-
# import tab
import os
import time

time = float(time.time())
print('Start ICMP Test! Please wait a monment!')


def ping_test():
    ips = open('IP_List.txt', 'r')  # 只读方式打开文本文件ip列表
    ip_true = open('Reachable.txt', 'w')  # 创建文本文件Reachable.txt'，w 表示只写，记录ping测成功的IP
    ip_false = open('Unreachable.txt', 'w')  # 创建文本文件Unreachable.txt'，w 表示只写，记录ping测失败的IP
    count_true, count_false = 0, 0
    for ip in ips.readlines():
        ip = ip.replace('\n', '')
        print('Start Ping %s' % ip)
        return1 = os.system('ping -c 3 %s' % ip)  # 使用操作工具ping测3个包，linux -c，windows -n
        if return1:
            print('Ping %s is Fail' % ip)
            ip_false.write(ip + '\n')
            count_false += 1
        else:
            print('Ping %s is OK' % ip)
            ip_true.write(ip + '\n')
            count_true += 1
    ip_true.close()
    ip_false.close()
    ips.close()
    print("The Numerber of Sucessful Tests:", count_true)
    print("The Numerber of Failed Tests:", count_false)


ping_test()
