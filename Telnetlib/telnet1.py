
#!/usr/bin/python
#-*- coding: utf-8 -*-
import re                                   # 引入正则表达式
import telnetlib                            # 引入telnetlib模块
import time                                 # 引入系统时间
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')               # 定义变量LogTime
time.sleep(1)                               # 系统等待1秒
tel1 = open('tel1.txt', 'w')                # 创建文本文件，w 表示只写，记录telnet成功的IP
tel2 = open('tel2.txt', 'w')                # 创建文本文件，w 表示只写，记录telnet失败的IP
count_True,count_False=0,0
username = input('username:')
password = input('password:')
for line in open("iplist.txt"):                   # 执行一个for循环，定义line 变量，打开access_list.txt文本，默认是r模式
        host = line.strip()                       # 定义一个变量host ，即IP地址,strip()方法移除字符串前后的空格
        print("Start telnet", host)               # 打印信息
        try:
                tn = telnetlib.Telnet(host)       # 调用telnetlib的Telnet函数，赋值给变量tn，以telnet方式登陆host
                time.sleep(1)                             # 等待2s，有时候系统反应慢。
                tn.read_until(b'Username:')                # 读到用户名交互信息，不同厂家的telnet交互信息不同。
                tn.write(username.encode() + b'\n')      # 输入用户名
                tn.read_until(b'Password:')               # 读到密码交互信息
                time.sleep(1)
                tn.write(password.encode() + b'\n')       # 输入密码
                time.sleep(1)
                for command in open("commands.txt"):      #执行循环，打开命令文本
                        cmd = command.replace('\n', '')
                        tn.write(cmd.encode() + b'\n')     # 发送cmd变量的命令给设备
                        time.sleep(2)
                telreply = tn.read_very_eager()            # 收集交互信息
                log = open(host + '-' + LogTime + '.txt', 'w')   # 创建一个变量log ,以w模式操作
                log.write(telreply.decode())             # 将交互信息写入log文件中
                log.close()                                       # 关闭log文件
                print(host, "Data Collect Successfully!")    # 打印提示信息。
                tel1.write(host+'\n')                        # 把host对应的ip地址记录到tel文本中
                count_True += 1
        except:
                print(host, 'Telnet Failed')
                tel2.write(host + '\n')
                count_False += 1
print('successfully logged in:',count_True)              # 打印登陆成功的设备数量
print('failed logged in:',count_False)                   # 打印登陆失败的设备数量