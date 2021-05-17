#!/usr/bin/python
#-*- coding: utf-8 -*-
import re
import telnetlib
import time
import paramiko  # 引入ssh模块，该模块需要单独安装；
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
t1 = open('tel1.txt', 'w')                  # 创建文本文件，w 表示只写,原有文件会被删除覆盖，记录telnet成功的IP
f1 = open('tel2.txt', 'w')
count_True,count_False=0,0                  # 定义两个变量，用来统计连接成功和失败的设备数量
username = ('banner')                       # 定义设备的用户名
password = ('Ops1@12345')                   # 定义设备密码
for line in open("core_list.txt"):          # 执行一个for循环，定义line 变量，打开core_list.txt文本，默认是r模式
        host = line.strip()                 # 定义一个变量host ，即IP地址,strip()方法移除字符串前后的空格
        ssh_port = 22                       # 配置ssh端口为22
        print("Start to connect", host)     # 打印字符串，提示开始连接设备
        try:
                client = paramiko.SSHClient()
                client.load_system_host_keys()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(host, port=ssh_port, username=username, password=password, timeout=10, look_for_keys=False)
                print("Successfully connected to ",host)
                remote_conn = client.invoke_shell()
                time.sleep(4)
                for command in open("commands.txt"):
                        cmd = command.replace('\n', '')
                        remote_conn.send(cmd.encode()+ b'\n' )
                        time.sleep(2)
                time.sleep(1)
                info = remote_conn.recv(99999999)
                log = open(host + '-' + LogTime + '.txt', 'w')
                log.write(info.decode())
                log.close()
                print(host,"Exec Commands Successfully")
                t1.write(host+'\n')
                count_True += 1
        except:
                print (host, 'Connect Failed !!')
                f1.write(host + '\n')
                count_False += 1
print('SSH Failed:',count_False)
print('SSH Successfully:',count_True)
