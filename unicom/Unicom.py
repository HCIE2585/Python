#!/usr/bin/python
import re
import telnetlib
import paramiko
import time
import os
import socket
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
count_True,count_False=0,0
time.sleep(1)
Device = input('''
Please Select Platform
1:Core
2:Access
Put Device ID:''')
if Device == '1':
        s1 = open('s1.txt', 'w')  # 创建文本文件，w 表示只写,原有文件会被删除覆盖，记录成功的IP
        f1 = open('f1.txt', 'w')
        username = "banner"
        password = "Ops1@12345"
        for line in open("hw_core_list.txt"):
                ip = line.strip()
                ssh_port = 22
                print("Start to connect", ip)
                try:
                        connet_client = paramiko.SSHClient()
                        connet_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        connet_client.connect(ip, ssh_port, username, password, timeout=5,look_for_keys=False)
                        shell_client = connet_client.invoke_shell()
                        time.sleep(2)
                        for cmd in open("hw_cmd.txt"):
                                command = cmd.strip()
                                shell_client.send(cmd.encode()+ b'\n')
                                time.sleep(2)
                        out = b''
                        while shell_client.recv_ready():
                                out += shell_client.recv(1024)
                        time.sleep(2)
                        log = open(ip + '-' + LogTime + '.txt', 'w')
                        time.sleep(2)
                        log.write(out.decode())
                        time.sleep(2)
                        log.close()
                        print(ip, "Exec Commands Successfully")
                        s1.write(ip + '\n')  # 把host对应的ip地址记录到tel文本中
                        count_True += 1
                except paramiko.ssh_exception.AuthenticationException:
                        print(ip, 'Authentication Failed')
                        f1.write(ip + '\n')
                        count_False += 1
                except socket.error:
                        print(ip, "is unreachable")
                        f1.write(ip + '\n')
                        count_False += 1
        for line in open("h3c_list.txt"):
                ip = line.strip()
                ssh_port = 22
                print("Start to connect", ip)
                try:
                        connet_client = paramiko.SSHClient()
                        connet_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        connet_client.connect(ip, ssh_port, username, password, timeout=5,look_for_keys=False)
                        shell_client = connet_client.invoke_shell()
                        time.sleep(2)
                        for cmd in open("h3c_cmd.txt"):
                                command = cmd.strip()
                                shell_client.send(cmd.encode()+ b'\n')
                                time.sleep(4)
                        out = b''
                        while shell_client.recv_ready():
                                out += shell_client.recv(1024)
                        time.sleep(4)
                        log = open(ip + '-' + LogTime + '.txt', 'w',encoding='gbk',errors='ignore')
                        time.sleep(4)
                        log.write(out.decode('gb18030'))
                        time.sleep(4)
                        log.close()
                        print(ip, "Exec Commands Successfully")
                        s1.write(ip + '\n')  # 把host对应的ip地址记录到tel文本中
                        count_True += 1
                except paramiko.ssh_exception.AuthenticationException:
                        print(ip, 'Authentication Failed')
                        f1.write(ip + '\n')
                        count_False += 1
                except socket.error:
                        print(ip, "is unreachable")
                        f1.write(ip + '\n')
                        count_False += 1
if Device == '2':
        s2 = open('s2.txt', 'w')  # 创建文本文件，w 表示只写,原有文件会被删除覆盖，记录成功的IP
        f2 = open('f2.txt', 'w')
        username = "banner"
        password = "Ops1@12345"
        for line in open("hw_access_list.txt"):  # 执行一个for循环，定义line 变量，打开access_list.txt文本，默认是r模式
                ip = line.strip()  # 定义一个变量host ，即IP地址,strip()方法移除字符串前后的空格
                print("Start telnet", ip)  # 打印信息
                try:
                        tn = telnetlib.Telnet(ip)  # 调用telnetlib的Telnet函数，赋值给变量tn，以telnet方式登陆host
                        time.sleep(1)  # 等待2s，有时候系统反应慢。
                        tn.read_until(b'Username:')  # 读到用户名交互信息，不同厂家的telnet交互信息不同。
                        tn.write(username.encode() + b'\n')  # 输入用户名
                        tn.read_until(b'Password:')  # 读到密码交互信息
                        time.sleep(1)
                        tn.write(password.encode() + b'\n')  # 输入密码
                        time.sleep(1)
                        for command in open("hw_cmd.txt"):  # 执行循环，打开命令文本
                            cmd = command.strip()
                            tn.write(cmd.encode() + b'\n')  # 发送cmd变量的命令给设备
                            time.sleep(2)
                        out_info = tn.read_very_eager()  # 收集交互信息
                        log = open(ip + '-' + LogTime + '.txt', 'w')  # 创建一个变量log ,以w模式操作
                        log.write(out_info.decode())  # 将交互信息写入log文件中
                        log.close()  # 关闭log文件
                        print(ip, "Data Collect Successfully!")  # 打印提示信息。
                        s2.write(ip + '\n')  # 把host对应的ip地址记录到tel文本中
                        count_True += 1
                except:
                        print(ip, 'Telnet connection failed')
                        f2.write(ip + '\n')
                        count_False += 1


