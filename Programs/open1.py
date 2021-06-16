#!/usr/bin/python
#file = open('iplist.txt','r')
#print (file.readline())


for line in open("iplist.txt"):                   # 执行一个for循环，定义line 变量，打开access_list.txt文本，默认是r模式
        print(line.strip())
        host = line.replace('\n', '')             # 定义一个变量host ，即IP地址
        print("Start telnet", host)               # 打印信息

#ip = open("iplist.txt",'r')
#for host in ip.readlines():
#        hostip = host.strip()
#        print(hostip)
