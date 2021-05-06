#!/usr/bin/python
#-*- coding: utf-8 -*-
import re
import paramiko          #引入ssh模块，该模块需要单独安装。
import time
from tkinter import *
#import tkMessageBox
class Application1(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLabel = Label(self,text='注意备份开始后需要输入TFTP服务器地址！')
        self.helloLabel.pack()
        self.quitButton = Button(self,text='开始运行程序',command=self.quit)
        self.quitButton.pack()
#        self.quitButton.grid()
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLabel = Label(self, text='备份完成！未成功部分请检查失败原因！')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='退出程序',command=sys.exit)
        self.quitButton.pack()
app1=Application1()
app1.master.title('配置备份工具')
app1.mainloop()
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
time.sleep(1)
print ('''
*****************************************************
***       Welcome to use this python script!      ***
***                          Author:Sun Jian      ***
***                          Date:2017-12-11      ***
*****************************************************''')
tftp = input('Please Enter TFTP Sever IP:')
print('Please wait for 2 seconds')
time.sleep(2)
Device = input('''
Please Select Device
1:HuaWei_Switch;
2:HillStone(E1700/M3108);
3:H3C;
Put Device ID:''')
time.sleep(2)
if Device == '1':
    print ('ICMP test begin!')
    time.sleep(2)
    import HW_icmp
    print ('ICMP test end!')
    time.sleep(2)
    action = raw_input('''
Please Select Action :
1:Config & Backup(not support);
2:Backup;
Put Your Choose:''')
    for line in open("HW_IP_True.txt"):
        hostname = line.replace('\n','')
        temp = open('HW_temp.txt','w')
        port = 22
        username = 'admin'
        password = 'passw0rd'
        if action == '2':
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(hostname, port, username, password, timeout=5)
                remote_conn = client.invoke_shell()
                remote_conn.send('display version\n')
                time.sleep(1)
                remote_conn.send('\n')
                out = remote_conn.recv(temp)
                DeviceName = (re.findall(str(".*<(.*)>.*"),out))[0]
                save = "save %s-%s.cfg " %(DeviceName,LogTime)
                remote_conn.send(save+'\n')
                time.sleep(1)
                remote_conn.send('y'+'\n')
                time.sleep(2)
                tftp_cli = "tftp %s put %s-%s.cfg" %(tftp,DeviceName,LogTime)
                remote_conn.send(tftp_cli+'\n')
                time.sleep(2)
                print  (hostname,'Backup Success !!')
            except :
                hostname,'Backup Failed !!'
    print('The program will be  closed after 5 seconds ')
    time.sleep(1)
    print('5')
    time.sleep(1)
    print('4')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
elif Device == '2':
    print ('ICMP test begin!')
    time.sleep(2)
    import Hillstone_icmp
    print ('ICMP test end!')
    time.sleep(2)
    action = raw_input('''Please Select Action :
        1:Config & Backup(not support);
        2:Backup;
    Put Your Choose:''')
    for line in open("HS_IP_True.txt"):
        hostname = line.replace('\n','')
        temp = open('HS_temp.txt','w')
        port = 22
        username = 'Admin_sxdd'
        password = 'CGcsxb@001$'
        if action == '2':
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(hostname, port, username, password, timeout=5)
                remote_conn = client.invoke_shell()
                remote_conn.send('show version \n')
                time.sleep(2)
                remote_conn.send('\n')
                out = remote_conn.recv(temp)
                time.sleep(2)
                DeviceName = (re.findall('.*(?=#)',out))[0]
                tftp_cli = "export configuration startup to tftp server %s %s-%s..cfg" %(tftp,DeviceName,LogTime)
                remote_conn.send(tftp_cli+'\n')
                time.sleep(2)
                print  (hostname,'Backup Success !!')
            except :
                print (hostname,'Backup Failed !!')
    print ('Thank you for use！The program will be closed after 5 seconds！')
    time.sleep(1)
    print('5')
    time.sleep(1)
    print('4')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
else:
    print ('Device not in list！')
app=Application()
app.master.title('配置备份工具')
app.mainloop()