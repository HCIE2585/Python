#!/usr/bin/python
# -*- coding:gb2312 -*-
#import tab
import time,os
time = float (time.time())
print('''
*****************************************************
***       Welcome to use my python script         ***
***                          Author:Sun Jian      ***
***                          Version:v1           ***
*****************************************************''')
def HS_1700_ping_test():
    ips = open('HS_1700_IP_List.txt','r')
    ip_True = open('HS_IP_True.txt','w')
    ip_False = open('HS_IP_False.txt','w')
    count_True,count_False=0,0
    for ip in ips.readlines():
        ip = ip.replace('\n','')
        print('start ping %s' % ip)
        return1= os.system('ping -c 3 %s'%ip)
        if return1 :
            print ('ping %s is fail'%ip)
            ip_False.write(ip+'\n')
            count_False += 1
        else:
            print ('ping %s is ok'%ip)
            ip_True.write(ip+'\n')
            count_True += 1
    ip_True.close()
    ip_False.close()
    ips.close()
#    end_Time = int(time.time())
#   print ("time(sencond):"),end_Time - start_time,"s"
#   print ("ping OK IP:"),count_True,"   ping False IP:",count_False
HS_1700_ping_test()


