#!/usr/bin/python
# -*- coding:gb2312 -*-
import time                                             #����ϵͳʱ��
from pythonping import ping
import os
time = float (time.time())
print('Start ICMP Test! Please wait a monment!')
ips = open('IP_List.txt', 'r')                          # ֻ����ʽ���ı��ļ�ips
ip_True = open('IP_True.txt', 'w')                      # �����ı��ļ�IP_True.txt��w ��ʾֻд����¼ping��ɹ���IP
ip_False = open('IP_False.txt', 'w')                    # �����ı��ļ�IP_False.txt��w ��ʾֻд����¼ping��ʧ�ܵ�IP
count_True,count_False=0,0
for ip_address in ips.readlines():
        host = ip_address.strip()
        print('Start Ping %s' % host)
        result = ping(host)
        if 'Reply' in str(result):
                                                        # �� pythonping �У�ping()����Ĭ�϶�Ŀ�� IP ��ַ ping 4 �Σ���Ŀ�� IP ��ַ�ɴ�ʱ��ping()�������ص��ǡ�Reply from x.x.x.x, x bytes in xx.xx ms����
                                                        # ping()��������ֵ��������һ������ pythonping.executor.ResponseList ���������ͣ�����Ϊ��ʹ�������in���жϣ�����ͨ��str()��������ת��
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


