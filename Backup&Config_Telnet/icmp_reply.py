#!/usr/bin/python
# -*- coding:gb2312 -*-
#import tab
import time,os
start_time = int (time.time())
#ICMP = raw_input('Please Enter Device ID:')
def hw_ping_test():
	ips = open('HW_IP_List.txt','r')
	ip_True = open('HW_IP_True.txt','w')
	ip_False = open('HW_IP_False.txt','w')
	count_True,count_False=0,0
	for ip in ips.readlines():
		ip = ip.replace('\n','')
		return1= os.system('ping -n 1 -w 1 %s'%ip)
		if return1 :
			print 'ping %s is fail'%ip
			ip_False.write(ip+'\n')
			count_False += 1
		else:
			print 'ping %s is ok'%ip
			ip_True.write(ip+'\n')
			count_True += 1
	ip_True.close()
	ip_False.close()
	ips.close()
	end_Time = int(time.time())
	print "time(sencond):",end_Time - start_time,"s"
	print "ping OK IP:",count_True,"   ping False IP:",count_False
hw_ping_test()
def HS_1700_ping_test():
    ips = open('HS_1700_IP_List.txt','r')
    ip_True = open('HS_IP_True.txt','w')
    ip_False = open('HS_IP_False.txt','w')
    count_True,count_False=0,0
    for ip in ips.readlines():
        ip = ip.replace('\n','')
        return1= os.system('ping -n 2 -w 1 %s'%ip)
        if return1 :
            print 'ping %s is fail'%ip
            ip_False.write(ip+'\n')
            count_False += 1
        else:
            print 'ping %s is ok'%ip
            ip_True.write(ip+'\n')
            count_True += 1
    ip_True.close()
    ip_False.close()
    ips.close()
    end_Time = int(time.time())
    print "time(sencond):",end_Time - start_time,"s"
    print "ping OK IP:",count_True,"   ping False IP:",count_False
HS_1700_ping_test()
def H3C_3620_ping_test():
    ips = open('3620_IP_List.txt','r')
    ip_True = open('3620_IP_True.txt','w')
    ip_False = open('3620_IP_False.txt','w')
    count_True,count_False=0,0
    for ip in ips.readlines():
        ip = ip.replace('\n','')
        return1= os.system('ping -n 2 -w 1 %s'%ip)
        if return1 :
            print 'ping %s is fail'%ip
            ip_False.write(ip+'\n')
            count_False += 1
        else:
            print 'ping %s is ok'%ip
            ip_True.write(ip+'\n')
            count_True += 1
    ip_True.close()
    ip_False.close()
    ips.close()
    end_Time = int(time.time())
    print "time(sencond):",end_Time - start_time,"s"
    print "ping OK IP:",count_True,"   ping False IP:",count_False
H3C_3620_ping_test()


