#!/usr/bin/python
#-*- coding: utf-8 -*-
import telnetlib
import time
username = ('admin')
password = ('admin')
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
for line in open("IP_True.txt"):                #执行一个循环，打开ip_True文件，所有需要telnet的设备ip
        host = line.replace('\n', '')
        print("Start telnet", host)
        username = ('admin')            #input device username
        password = ('snmsss8')            #input device password
        try:
                tn = telnetlib.Telnet(host)
                time.sleep(1)           #系统睡一会，不然有时候反应不过来
                tn.read_until(b'login')                 # 不同厂家显示信息不一样，读取到该信息，输入用户名
                tn.write(username.encode()+ b'\n')
                tn.read_until(b'Password')              # 不同厂家显示信息不一样，读取到该信息，输入密码
                time.sleep(1)
                tn.write(password.encode()+ b'\n')
                time.sleep(1)
                for command in open("commands.txt"):             #执行一个循环，打开commands.txt文件，该文件包含需要运行的命令
                        try:
                                cmd = command.replace('\n', '')
                                tn.write(cmd.encode()+ b'\n' )
                                time.sleep(4)
                        except:
                                print('Failed')
                telreply = tn.read_very_eager()
                log = open(host + '-' + LogTime + '.txt', 'w')          #
                log.write(telreply.decode())
                log.close()
                print(host, "Data Collect Successfully!")
        except:
                print(host, 'Telnet Failed')