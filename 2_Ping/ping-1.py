#!/usr/bin/python
# -*- coding:gb2312 -*-
# import tab
import os
import time

time = float(time.time())
print('Start ICMP Test! Please wait a monment!')


def ping_test():
    ips = open('IP_List.txt', 'r')  # ֻ����ʽ���ı��ļ�ip�б�
    ip_true = open('Reachable.txt', 'w')  # �����ı��ļ�Reachable.txt'��w ��ʾֻд����¼ping��ɹ���IP
    ip_false = open('Unreachable.txt', 'w')  # �����ı��ļ�Unreachable.txt'��w ��ʾֻд����¼ping��ʧ�ܵ�IP
    count_true, count_false = 0, 0
    for ip in ips.readlines():
        ip = ip.replace('\n', '')
        print('Start Ping %s' % ip)
        return1 = os.system('ping -c 3 %s' % ip)  # ʹ�ò�������ping��3������linux -c��windows -n
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
