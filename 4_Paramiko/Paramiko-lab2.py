#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import paramiko
import sys  # 导入sys模块，是系统内建模块，为了使用sys.argv
import socket

LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
username = 'cisco'
password = 'cisco'
ip_file = sys.argv[1]  # 定义一个变量ip_file对应sys.argv[1]
cmd_file = sys.argv[2]  # 定义一个变量cmd_file对应sys.argv[2]
iplist = open(ip_file, 'r')  # 将ip_file的内容赋值给变量iplist
t1 = open('lab2_Successful.txt', 'w')  # 创建文本文件，w 表示只写,原有文件会被删除覆盖，记录ssh成功的IP
f1 = open('lab2_Failed.txt', 'w')
count_False, count_True = 0, 0
for line in iplist.readlines():
    host = line.strip()
    ssh_port = 22
    print("Start to connect", host)
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, port=ssh_port, username=username, password=password, timeout=20, look_for_keys=False)
        remote_conn = client.invoke_shell()
        time.sleep(2)
        cmdlist = open(cmd_file, 'r')  # 只读方式打开文件，'r'模式只能打开已存在的文件，如果文件不存在，会报错
        for command in cmdlist.readlines():
            cmd = command.strip()
            remote_conn.send(cmd.encode() + b'\n')
            time.sleep(5)
        time.sleep(1)
        info = remote_conn.recv(999999999)
        time.sleep(2)
        log = open(host + '-' + LogTime + '.txt', 'w')
        time.sleep(2)
        log.write(info.decode('ascii'))
        time.sleep(2)
        log.close()
        print(host, "Exec Commands Successfully")
    except paramiko.ssh_exception.AuthenticationException:
        f1.write(host + '\n')  # 把主机地址写到tel2.txt中
        count_False += 1  # 统计执行失败的数量，每次加1
        print(host, 'Authentication Failed')
    except socket.error:
        print(host, "is unreachable")
        f1.write(host + '\n')  # 把主机地址写到tel2.txt中
        count_False += 1  # 统计执行失败的数量，每次加1
