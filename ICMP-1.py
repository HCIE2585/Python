#!/usr/bin/python
# -*- coding:gb2312 -*-
#import tab
import time,os          #����ϵͳ������ʱ��
time = float (time.time())
print('Start ICMP Test! Please wait a monment!')
def ping_test():
        ips = open('IP_List.txt', 'r')           # ֻ����ʽ���ı��ļ�ips
        ip_True = open('IP_True.txt', 'w')               #�����ı��ļ�IP_True.txt��w ��ʾֻд����¼ping��ɹ���IP
        ip_False = open('IP_False.txt', 'w')             ##�����ı��ļ�IP_False.txt��w ��ʾֻд����¼ping��ʧ�ܵ�IP
        count_True,count_False=0,0
        for ip in ips.readlines():
                ip = ip.replace('\n','')
                print('Start Ping %s' % ip)
                return1= os.system('ping -c 3 %s'%ip)
                if return1 :
                        print ('Ping %s is Fail'%ip)
                        ip_False.write(ip+'\n')
                        count_False += 1
                else:
                        print ('Ping %s is OK'%ip)
                        ip_True.write(ip+'\n')
                        count_True += 1
        ip_True.close()
        ip_False.close()
        ips.close()
        print ("The Numerber of Sucessful Tests:",count_True)
        print ("The Numerber of Failed Tests:",count_False)
ping_test()


