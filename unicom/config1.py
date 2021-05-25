#!/usr/bin/python
#-*- coding: utf-8 -*-
import re
import telnetlib
import time
import paramiko  # 引入ssh模块，该模块需要单独安装；
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
time.sleep(1)
print ('''
*****************************************************
***       Welcome to use this python script!      ***
***                          Author:Banner        ***
***                                               ***
*****************************************************''')
Device = input('''
Please Select Device
1:Core
2:Access
Put Device ID:''')
if Device == '1':
        username = ('banner')
        password = ('Ops1@12345')
if Device == '2':
        username = ('unicom')
        password = ('Unicom@321')
protocol = input('''
Please Select protocol
1:Telnet
2:SSH
Put protocol ID:''')
count_True,count_False=0,0
if Device == '1':
        t1 = open('t1.txt', 'w')  # 创建并打开文本文件t1，w 表示只写，记录core_list连接成功的IP
        f1 = open('f1.txt', 'w')  # 创建并打开文本文件f1，w 表示只写，记录core_list连接失败的IP
        if protocol == '1':             # telnet
                for line in open("H3C_device.txt"):
                        host = line.strip()     # 使用strip（）方法移除前后空格
                        print("Start telnet", host)
                        try:
                                tn = telnetlib.Telnet(host)
                                time.sleep(4)
                                tn.read_until(b'Username:')       # 读到交互信息
                                tn.write(username.encode() + b'\n')
                                tn.read_until(b'Password:')
                                time.sleep(4)
                                tn.write(password.encode() + b'\n')
                                time.sleep(1)
                                for command in open("commands.txt"):
                                        cmd = command.replace('\n', '')   # 跟使用strip()类似，移除前后空格
                                        tn.write(cmd.encode() + b'\n')
                                        time.sleep(3)
                                telreply = tn.read_very_eager()
                                log = open(host + '-' + LogTime + '.txt', 'w')
                                log.write(telreply.decode())
                                log.close()
                                print(host, "Data Collect Successfully!")
                                t1.write(host+'\n')
                                count_True += 1
                        except:
                                print(host, 'Telnet Failed')
                                f1.write(host + '\n')
                                count_False += 1
                for line in open("core_list.txt"):
                        host = line.strip()     # 使用strip（）方法移除前后空格
                        print("Start telnet", host)
                        try:
                                tn = telnetlib.Telnet(host)
                                time.sleep(4)
                                tn.read_until(b'Username:')       # 读到交互信息
                                tn.write(username.encode() + b'\n')
                                tn.read_until(b'Password:')
                                time.sleep(4)
                                tn.write(password.encode() + b'\n')
                                time.sleep(1)
                                for command in open("commands.txt"):
                                        cmd = command.replace('\n', '')   # 跟使用strip()类似，移除前后空格
                                        tn.write(cmd.encode() + b'\n')
                                        time.sleep(3)
                                telreply = tn.read_very_eager()
                                log = open(host + '-' + LogTime + '.txt', 'w')
                                log.write(telreply.decode())
                                log.close()
                                print(host, "Data Collect Successfully!")
                                t1.write(host+'\n')
                                count_True += 1
                        except:
                                print(host, 'Telnet Failed')
                                f1.write(host + '\n')
                                count_False += 1
                print('Telnet Failed:',count_False)
                print('Telnet Successfully:',count_True)
        if protocol == '2':
                for line in open("H3C_FW.txt"):        #iplist
                        host = line.strip()
                        ssh_port = 22
                        print("Start to connect", host)
                        try:
                                client = paramiko.SSHClient()
                                client.load_system_host_keys()
                                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                                time.sleep(1)
                                client.connect(host, port=ssh_port, username=username, password=password, timeout=20, look_for_keys=False)
                                time.sleep(1)
                                remote_conn = client.invoke_shell()
                                time.sleep(2)
                                for command in open("h3c-commands.txt"):
                                        cmd = command.strip()
                                        print(cmd)
                                        remote_conn.send(cmd+ '\n')
                                        time.sleep(2)
                                        print('ssss')
                                time.sleep(1)
                                info = remote_conn.recv(99999999)
                                print (info)
                                log = open(host + '-' + LogTime + '.txt', 'w')
                                log.write(info.decode())
                                print("3")
                                time.sleep(2)
                                log.close()
                                print(host,"Exec Commands Successfully")
                                t1.write(host+'\n')
                                count_True += 1
                        except:
                                print (host, 'Connect Failed !!')
                                f1.write(host + '\n')
                                count_False += 1
                for line in open("core_list.txt"):        #iplist
                        host = line.strip()
                        ssh_port = 22
                        print("Start to connect", host)
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
if Device == '2':
        t2 = open('t2.txt', 'w')  # 创建并打开文本文件t2，w 表示只写，记录access_list连接成功的IP
        f2 = open('f2.txt', 'w')  # 创建并打开文本文件f2，w 表示只写，记录access_list连接成功的IP
        if protocol == '1':
                for line in open("access_list.txt"):
                        host = line.strip()
                        print("Start telnet", host)
                        try:
                                tn = telnetlib.Telnet(host)
                                time.sleep(2)
                                tn.read_until(b'Username:')       # 读到交互信息
                                tn.write(username.encode() + b'\n')
                                tn.read_until(b'Password:')
                                time.sleep(2)
                                tn.write(password.encode() + b'\n')
                                time.sleep(1)
                                for command in open("commands.txt"):
                                        cmd = command.replace('\n', '')
                                        tn.write(cmd.encode() + b'\n')
                                        time.sleep(2)
                                telreply = tn.read_very_eager()
                                log = open(host + '-' + LogTime + '.txt', 'w')
                                log.write(telreply.decode())
                                log.close()
                                print(host, "Data Collect Successfully!")
                                t2.write(host+'\n')
                                count_True += 1
                        except:
                                print(host, 'Telnet Failed')
                                f2.write(host + '\n')
                                count_False += 1
                print('Telnet Failed:',count_False)
                print('Telnet Successfully:',count_True)
        if protocol == '2':
                for line in open("access_list.txt"):        #iplist
                        host = line.strip()      #
                        ssh_port = 22
                        print("Start to connect", host)
                        try:
                                client = paramiko.SSHClient()
                                client.load_system_host_keys()
                                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                                client.connect(host, port=ssh_port, username=username, password=password, timeout=10, look_for_keys=False)
                                print("Successfully connected to ",host)
                                remote_conn = client.invoke_shell()
                                time.sleep(2)
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
                                t2.write(host+'\n')
                                count_True += 1
                        except:
                                print (host, 'Connect Failed !!')
                                f2.write(host + '\n')
                                count_False += 1
                print('SSH Failed:',count_False)
                print('SSH Successfully:',count_True)
