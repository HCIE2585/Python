#!/usr/bin/python
#coding=utf-8
import telnetlib
import time
import re
from Tkinter import *
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
app = Application()
app.master.title('Hello World')
app.mainloop()
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
Device = raw_input('''Please Select Device
    1:HuaWei;
    2:HillStone(E1700/M3108);
    3:H3C-3620;
    4:Cisco
Put Device ID:''')
tftp = raw_input('Please Enter TFTP Sever IP:')
if Device == '1':                                                    #华为相关
    import HW_icmp
    action = raw_input('''Please Select Action :
        1:Config & Backup;
        2:Backup;
    Put Your Choose:''')
    for line in open("HW_IP_True.txt"):
        Host = line.replace('\n','')
        UserName = 'admin'
        PassWord = 'passw0rd'
        save = 'save'
        super = 'huawei,123'
        display = 'display cur'
        try:
            tn = telnetlib.Telnet(Host)
            tn.read_until('Username:')            #调用AAA用户
            tn.write(UserName+'\n')
            tn.read_until('Password:')            #直接调用vty下密码可以忽略username部分
            tn.write(PassWord+'\n')
            time.sleep(1)
            #tn.write('super'+'\n')     #如果配置了super密码 启用该部分代码即可
            #time.sleep(1)
            #tn.read_until('Password:')
            #tn.write(super+'\n')
            if action == '1' :
                config = open("hw_script.txt",'r')
                for conf in config.readlines():                            #配置脚本
                    tn.write(conf+'\n')
                tn.write(b'\n')
                telreply = tn.expect([],timeout=1)[2].encode("utf-8")      #获取Telnet交互信息
                DeviceName = (re.findall(str(".*<(.*)>.*"),telreply))[0]  #生成的设备名称是个list。后面调用列表里面的索引0
                tn.write(save+' '+DeviceName+'-'+LogTime+'.cfg'+'\n')
                tn.read_until('N]')
                tn.write('y'+'\n')
                tn.read_until('successfully.')
                tn.write('tftp'+' '+tftp+' '+'put'+' '+'flash:/'+DeviceName+'-'+LogTime+'.cfg'+'\n' )#使用tftp导出系统配置
                time.sleep(2)
                tn.write('quit'+'\n')
                tn.close()
                print Host,'Config & Backup Success !!'
            elif action == '2':
                tn.write(b'\n')
                telreply = tn.expect([],timeout=1)[2].encode("utf-8")      #获取Telnet交互信息
                DeviceName = (re.findall(str(".*<(.*)>.*"),telreply))[0]  #生成的设备名称是个list。后面调用列表里面的索引0
                tn.write(save+' '+DeviceName+'-'+LogTime+'.cfg'+'\n')
                tn.read_until('N]')
                tn.write('y'+'\n')
                tn.read_until('successfully.')
                tn.write('tftp'+' '+tftp+' '+'put'+' '+DeviceName+'-'+LogTime+'.cfg'+'\n' )#使用tftp导出系统配置
                time.sleep(2)
                #except :
                #   tn.write('tftp'+' '+tftp+' '+'put'+' '+DeviceName+'-'+LogTime+'.cfg'+'\n' )
                #  time.sleep(2)
                tn.write('quit'+'\n')
                tn.close()
                print Host,'Backup Success !!'
        except :
            print Host,'Backup Failed !!'
elif Device == '2':                                        #山石相关
    import Hillstone_icmp
    action = raw_input('''Please Select Action :
        1:Config & Backup;
        2:Backup;
    Put Your Choose:''')
    for line in open("HS_IP_True.txt"):
        Host = line.replace('\n','')
        UserName = 'sxddsn'
        PassWord = 'sn!@#'
        Quit = 'exit'
        if action == '1':                        #备份和配置更改
            try:
                tn = telnetlib.Telnet(Host)
                tn.read_until('login:')
                tn.write(UserName+'\n')
                tn.read_until('password:')
                tn.write(PassWord+'\n')
                tn.read_until('#')
                tn.write('configure'+'\n')
                time.sleep(1)
                tn.write('interface ethernet0/2'+'\n')
                time.sleep(1)
                tn.write('manmge ssh'+'\n')
                #tn.write('language en'+'\n')
                #time.sleep(1)
                #tn.write('admin user Admin_sxdd'+'\n')
                #time.sleep(1)
                #tn.write('access telnet'+'\n')
                time.sleep(1)
                #tn.write('access ssh'+'\n')
                #time.sleep(1)
                #tn.write('access https'+'\n')
                #time.sleep(1)
                #tn.write('password CGcsxb@001$'+'\n')
                #time.sleep(1)
                tn.write(Quit+'\n')
                time.sleep(1)
                tn.write(Quit+'\n')
                time.sleep(1)
                tn.write('save'+'\n')
                tn.read_until('[y]/n:')
                tn.write('\n')
                tn.read_until('y/[n]:')
                tn.write('y')
                time.sleep(1)
                tn.write('show version'+'\n')
                time.sleep(1)
                telreply = tn.expect([],timeout=1)[2].encode("utf-8")
                time.sleep(2)
                DeviceName = re.findall('.*(?=# show version)',telreply)[0]
                time.sleep(1)
                #tn.write('export configuration startup to tftp server'+' '+tftp+' '+DeviceName+'-'+LogTime+'.cfg'+'\n' )
                #time.sleep(2)
                tn.write('exit'+'\n')
                tn.close()
                print Host,'Config & Backup Success !!'
            except :
                print Host,'Config & Backup Failed !!'
        elif action == '2':                         #备份
            try:
                tn = telnetlib.Telnet(Host)
                tn.read_until('login:')
                tn.write(UserName+'\n')
                tn.read_until('password:')
                tn.write(PassWord+'\n')
                time.sleep(1)
                tn.write('show version'+'\n')
                telreply = tn.expect([],timeout=1)[2].encode("utf-8")
                time.sleep(2)
                DeviceName = re.findall('.*(?=# show version)',telreply)[0]
                time.sleep(1)
                tn.write('export configuration startup to tftp server'+' '+tftp+' '+DeviceName+'-'+LogTime+'.cfg'+'\n' )
                time.sleep(2)
                tn.write('exit'+'\n')
                tn.close()
                print Host,'Backup Success !!'
            except :
                print Host,'Backup Failed !!'
elif Device == '3':
    import H3C_icmp
    action = raw_input('''Please Select Action :
        1:Config & Backup;
        2:Backup;
    Put Your Choose:''')
    for line in open("3620_IP_True.txt"):
        Host = line.replace('\n','')
        UserName = 'sxddsb'
        PassWord = 'sbqwe'
        save = 'save'
        try:
            tn = telnetlib.Telnet(Host)
            tn.read_until('login:')
            tn.write(UserName+'\n')
            tn.read_until('Password:')
            tn.write(PassWord+'\n')
            tn.write('super'+'\n')
            tn.read_until('Password:')
            tn.write(PassWord+'\n')
            if action == '1':
                config = open("hw_script.txt",'r')
                for conf in config.readlines():                            #配置脚本
                    tn.write(conf+'\n')
                tn.write(b'\n')
                telreply = tn.expect([],timeout=1)[2].encode("utf-8")      #获取Telnet交互信息
                DeviceName = (re.findall(str(".*<(.*)>.*"),telreply))[0]   #生成的设备名称是个list。后面调用列表里面的索引0
                tn.write('save cfa0:/'+DeviceName+'-'+LogTime+'.cfg'+'\n')
                tn.read_until('[Y/N]:')
                tn.write('y'+'\n')
                tn.write('\n')
                tn.write('tftp'+' '+tftp+' '+'put'+' '+DeviceName+'-'+LogTime+'.cfg'+'\n' )   #使用tftp导出系统配置
                tn.close()
                print Host,'Backup Success !!'
            elif action == '2':
                tn.write(b'\n')
                telreply = tn.expect([],timeout=1)[2].encode("utf-8")      #获取Telnet交互信息
                DeviceName = (re.findall(str(".*<(.*)>.*"),telreply))[0]  #生成的设备名称是个list。后面调用列表里面的索引0
                tn.write('save cfa0:/'+DeviceName+'-'+LogTime+'.cfg'+'\n')
                tn.read_until('[Y/N]:')
                tn.write('y'+'\n')
                tn.write('\n')
                tn.write('tftp'+' '+tftp+' '+'put'+' '+DeviceName+'-'+LogTime+'.cfg'+'\n' )   #使用tftp导出系统配置
                time.sleep(2)
                tn.close()
                print Host,'Backup Success !!'
        except :
            print Host,'Backup Failed !!'
else :
    print 'Device not in list！'