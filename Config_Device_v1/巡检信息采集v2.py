#!/usr/bin/python
#-*- coding: utf-8 -*-
import re
import paramiko          #引入ssh模块，该模块需要单独安装。
import telnetlib
import time
from tkinter import *
#import tkMessageBox
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
time.sleep(1)
print ('''
*****************************************************
***       Welcome to use this python script!      ***
***                          Author:Banner        ***
***                          Date:2020-02-02      ***
*****************************************************''')
tftp = input('Please Enter TFTP Sever IP:')
print('Please wait for 2 seconds')
time.sleep(2)
Device = input('''
Please Select Platform
1:CISCO-IOS
2:HuaWei_Switch;
3:HillStone
4:H3C;
Put Device ID:''')
time.sleep(1)
if Device == '1':
        print ('ICMP test begin!')
        time.sleep(1)
        import icmp
        print ('ICMP test end!')
        time.sleep(1)
        protocol = input('''
Please Select login protocol :
1:ssh;
2:telnet;
Put Your Choose:''')
        for line in open("IP_True.txt"):
                host = line.replace('\n','')
                temp = open('temp.txt','w')
                ssh_port = 22
                username = input('admin')
                password = input('admin')
                if protocol == '1':
                        try:
                                print("Start SSH", host)
                                client = paramiko.SSHClient()
                                client.load_system_host_keys()
                                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                                client.connect(host, ssh_port, username, password)
                                remote_conn = client.invoke_shell()
                                stdin, stdout, stderr = client.exec_command('display version ')
                                print(stdout.read().decode())
                                remote_conn.send('display version'+'\n')
                                print (remote_conn.recv)
                                time.sleep(1)
                                print('test1')
#                                remote_conn.send('\n')
                                out = remote_conn.recv(temp)
                                print('test2')
                                DeviceName = (re.findall(str(".*<(.*)>.*"),out))[0]
                                print (DeviceName)
                                save = "save %s-%s.cfg " %(DeviceName,LogTime)
                                remote_conn.send(save+'\n')
                                time.sleep(1)
                                remote_conn.send('y'+'\n')
                                time.sleep(2)
                                tftp_cli = "tftp %s put %s-%s.cfg" %(tftp,DeviceName,LogTime)
                                remote_conn.send(tftp_cli+'\n')
                                time.sleep(2)
                                print  (host,'Backup Success !!')
                        except :
                                host,'Backup Failed !!'
                if protocol == '2':
                        for line in open("ip_True.txt"):
                                print ("Start telnet", host)
                                try:
                                        tn = telnetlib.Telnet(host)
                                        time.sleep(1)
                                        tn.read_until('Username:')
                                        tn.write(username.encode() + '\n')
                                        tn.write(password + '\n')
                                        for command in open("ios_cmd.txt"):
                                                try:
                                                        cmd = command.replace('\n', '')
                                                        tn.write(cmd.encode() + '\n')
                                                        time.sleep(1)
                                                except:
                                                        print (cmd, 'not found')
                                        telreply = tn.expect([], timeout=1)[2].encode("utf-8")
                                        DeviceName = (re.findall(str(".*<(.*)>.*"), telreply))[0]
                                        tn.close()
                                        log = open(DeviceName + '-' + LogTime + '.txt', 'w')
                                        log.write(telreply)
                                        log.close()
                                        print (host, "Data Collect Successfully!")
                                except:
                                        print (host, 'Telnet Failed')
        print('The program will be closed ! ')
        time.sleep(1)
        print('bye')
else:
        print ('Device not in list！')
