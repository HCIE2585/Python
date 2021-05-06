#!/usr/bin/python
#-*- coding: utf-8 -*-
import re
import paramiko          #引入ssh模块，该模块需要单独安装；
import time
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
time.sleep(1)
for line in open("IP_True.txt"):
        host = line.replace('\n', '')
        ssh_port = 22
        username = ('admin')
        password = ('snmsss8')
        print("Start to connect", host)
        try:
                client = paramiko.SSHClient()
                client.load_system_host_keys()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(host, ssh_port, username, password, timeout=5)
                remote_conn = client.invoke_shell()
                time.sleep(2)
                for command in open("commands.txt"):
                        cmd = command.replace('\n', '')
                        remote_conn.send(cmd.encode()+ b'\n' )
                        time.sleep(3)
                time.sleep(1)
                info = remote_conn.recv(99999999)
                log = open(host + '-' + LogTime + '.txt', 'w')
                log.write(info.decode())
                log.close()
                print(host,"Exec commands Success !!")
        except:
                print (host, 'Connect Failed !!')