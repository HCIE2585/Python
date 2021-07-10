#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import time  # 引入time模块，主要是为了使用sleep()方法,解决一些命令在直行过程中响应不及时的问题
import paramiko  # 引入ssh模块，该模块需要单独安装；

LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
t1 = open('lab1_Successful.txt', 'w')  # 创建文本文件，w 表示只写,原有文件会被删除覆盖，记录ssh成功的IP
f1 = open('lab2_Failed.txt', 'w')
count_True, count_False = 0, 0  # 定义两个变量，用来统计连接成功和失败的设备数量
username = 'cisco'  # 定义设备的用户名
password = 'cisco'  # 定义设备密码
for line in open("lab1_list.txt"):  # 执行一个for循环，定义line 变量，打开core_list.txt文本，默认是r模式
    host = line.strip()  # 定义一个变量host ，即IP地址,strip()方法移除字符串前后的空格
    ssh_port = 22  # 配置ssh端口为22
    print("Start to connect", host)  # 打印字符串，提示开始连接设备
    try:
        client = paramiko.SSHClient()  # 调用paramiko的SSHClient()方法，赋值给变量client
        client.load_system_host_keys()  # 指定远程主机的公钥文件，默认为.ssh目录下的known_hosts文件，本案例中可以不用
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 让paramiko接受来自服务端的公钥，任何时候都需要的配置
        client.connect(host, port=ssh_port, username=username, password=password, timeout=10,
                       look_for_keys=False)  # 使用paramiko.SSHClient()的connect()函数进行登陆，地址，端口，用户名和密码，超时时间，look_for_keys=False表示禁用在~/.ssh中搜索私钥文件。
        print("Successfully connected to ", host)  # 打印回显，提示连接成功。
        remote_conn = client.invoke_shell()  # 使用paramiko.SSHClient()的invoke_shell()来唤醒shell，就是cli配置界面
        time.sleep(2)  # 等待2s
        for command in open("lab1_cmds.txt"):  # 循环执行命令，
            cmd = command.replace('\n', '')
            remote_conn.send(cmd.encode() + b'\n')
            time.sleep(2)  # 等两秒，这个根据情况定，有时候有的命令输出慢。
        time.sleep(1)
        info = remote_conn.recv(99999999)  # 使用recv()函数将回显结果保存到info变量中
        log = open(host + '-' + LogTime + '.txt', 'w')  # 定义个log文本文件，
        log.write(info.decode())  # 把info信息写到log中，
        log.close()  # 关闭log文件
        print(host, "Exec Commands Successfully")  # 打印执行结果
        t1.write(host + '\n')  # 把主机地址写到tel1.txt中
        count_True += 1  # 统计执行成功的数量，每次加1
    except paramiko.ssh_exception.AuthenticationException:
        f1.write(host + '\n')  # 把主机地址写到tel2.txt中
        count_False += 1  # 统计执行失败的数量，每次加1
        print(host, 'Authentication Failed')
    except socket.error:
        print(host, "is unreachable")
        f1.write(host + '\n')  # 把主机地址写到tel2.txt中
        count_False += 1  # 统计执行失败的数量，每次加1
print('SSH Failed:', count_False)
print('SSH Successfully:', count_True)
