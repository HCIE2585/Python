#!/usr/bin/python
#-*- coding: utf-8 -*-
import re
import time                                 # 引入time模块，主要是为了使用sleep()方法,解决一些命令在直行过程中响应不及时的问题
import paramiko                             # 引入ssh模块，该模块需要单独安装；
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
print ('''
**********************************************************************************************************
***       Welcome to use this python script!                                                           ***
***                                                                                                    ***
***   1、只适用ssh登陆，使用paramiko库，可能会有一些问题                                                   ***
***   2、系统会自动创建t1.txt和f1.txt,统计失败和成功的地址                                                 ***
***   3、提前准备好lab3_hw_list.txt和lab3_hw_cmd.txt,一个存设备地址，一个存命令                            ***
***   4、如果收集的信息较多，需要在命令文本中增加不分屏显示命令。                                          ***
**********************************************************************************************************''')
time.sleep(10)
print ('''
系统5秒后开始执行,需要输入SSH用户名和密码
''')

t1 = open('result1.txt', 'w')
f1 = open('result2.txt', 'w')
count_True,count_False=0,0
username = input('Username:')
password = input('Password:')
for line in open("lab3_hw_list.txt"):
        host = line.strip()
        ssh_port = 22
        print("Start to connect", host)
        try:
                client = paramiko.SSHClient()
                client.load_system_host_keys()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(host, port=ssh_port, username=username, password=password, timeout=10, look_for_keys=False)
                time.sleep(1)
                print("Successfully connected to ",host)
                remote_conn = client.invoke_shell()
                time.sleep(2)
                for command in open("lab3_hw_cmd.txt"):
                        cmd = command.strip()
                        remote_conn.send(cmd.encode()+ b'\n' )
                        time.sleep(10)
                time.sleep(1)
                # out = remote_conn.recv(99999999)
                out =b''
                while remote_conn.recv_ready():
                        out += remote_conn.recv(1024)
                # print(out)
                log = open(host + '-' + LogTime + '.txt', 'wb')
                log.write(out)
                time.sleep(5)
                log.close()
                print(host,"Exec Commands Successfully")
                t1.write(host+'\n')
                count_True += 1
        except:
                print (host, 'Connect Failed !!')
                f1.write(host + '\n')
                count_False += 1
print('Connected Successfully:',count_True,'Please check result1.txt')
print('Connected Failed:',count_False,'Please check result2.txt')
