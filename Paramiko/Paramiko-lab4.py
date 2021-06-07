#!/usr/bin/python
#-*- coding: utf-8 -*-
import re
import time
import paramiko
import sys                                  # 导入sys模块，是系统内建模块，为了使用sys.argv
import getpass                              # 引入交互，主要是为了加密密码
import socket
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
username = input('username：')
password = getpass.getpass('Password:')     #
ip_file = sys.argv[1]                       # 定义一个变量ip_file对应sys.argv[1]
cmd_file = sys.argv[2]                      # 定义一个变量cmd_file对应sys.argv[2]
iplist = open(ip_file,'r')                  # 将ip_file的内容赋值给变量iplist
for line in iplist.readlines():
        host = line.strip()
        ssh_port = 22
        print("Start to connect", host)
        try:
                client = paramiko.SSHClient()
                client.load_system_host_keys()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(host, port=ssh_port, username=username, password=password, timeout=20, look_for_keys=False)
                remote_conn = client.invoke_shell()
                time.sleep(2)
                cmdlist = open(cmd_file, 'r')
                cmdlist.seek(0)
                for command in cmdlist.readlines():
                        cmd = command.strip()
                        remote_conn.send(cmd.encode()+ b'\n' )
                        time.sleep(5)
                time.sleep(1)
                out =b''
                while remote_conn.recv_ready():
                        out += remote_conn.recv(1024)
                # print(out)
                time.sleep(2)
                log = open(host + '-' + LogTime + '.txt', 'w')
                print('look at me')
                time.sleep(2)
                log.write(out.decode())
                time.sleep(5)
                log.close()
                print(host,"Exec Commands Successfully")
        except paramiko.ssh_exception.AuthenticationException:
                print (host, '认证失败')
        except socket.error:
                print (host,"主机不可达")
