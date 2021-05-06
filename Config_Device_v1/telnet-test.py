#!/usr/bin/python
#-*- coding: utf-8 -*-
import telnetlib
import time
username = ('admin')
password = ('admin')
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
for line in open("ip_True.txt"):
        host = line.replace('\n', '')
        print("Start telnet", host)
        tn = telnetlib.Telnet(host)
        time.sleep(1)
        tn.write(username.encode()+ b'\n')
        tn.write(password.encode()+ b'\n')
        for command in open("ios_cmd.txt"):
                try:
                        cmd = command.replace('\n', '')
                        tn.write(cmd.encode()+ b'\n' )
                        time.sleep(4)
                except:
                        print(cmd, 'not found')
        telreply = tn.read_very_eager()
#        tn.close()
        log = open(host + '-' + LogTime + '.txt', 'w')
        log.write(telreply.decode())
        log.close()
        print(host, "Data Collect Successfully!")
#    except:
#        print(host, 'Telnet Failed')
