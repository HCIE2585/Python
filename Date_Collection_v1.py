#!/usr/bin/python
#-*- coding: utf-8 -*-
import re                # 引入正则表达式
import telnetlib         # 引入telnet模块
import time
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
time.sleep(1)
print ('''
*****************************************************
***       Welcome to use this python script!      ***
***                          Author:Banner        ***
***                          Date:2020-02-02      ***
*****************************************************''')
import ICMP-1                 # 引入icmp测试脚本，对所有ip进行ping测，成功的再进行登陆；
for line in open("IP_True.txt"):
        host = line.replace('\n', '')
        print("Start telnet", host)
        try:
                tn = telnetlib.Telnet(host)
                time.sleep(1)
                tn.read_until(b'login')       # 读到交互信息
                tn.write(username.encode() + b'\n')
                tn.read_until(b'Password')
                time.sleep(1)
                tn.write(password.encode() + b'\n')
                time.sleep(1)
                for command in open("commands.txt"):
                        cmd = command.replace('\n', '')
                        tn.write(cmd.encode() + b'\n')
                        time.sleep(4)
                telreply = tn.read_very_eager()
                log = open(host + '-' + LogTime + '.txt', 'w')
                log.write(telreply.decode())
                log.close()
                print(host, "Data Collect Successfully!")
        except:
                print(host, 'Telnet Failed')
