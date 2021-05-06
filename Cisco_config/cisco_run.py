#!/usr/bin/python
import telnetlib
import time
import re
import icmp_reply
LogTime = time.strftime('%Y-%m-%d_%H:%M:%S')
for line in open("ip_True.txt"):
        Host = line
        CMD = 'show run'
        UserName = 'cisco'
        PassWord = 'cisco'
	Exit = 'exit'
        tn=telnetlib.Telnet(Host)
        tn.write(UserName.encode()+'\n')
        tn.write(PassWord.encode()+'\n')
        tn.write('enable'.encode()+'\n')
        tn.write('ccie'.encode()+'\n')
        tn.write('terminal length 0'.encode()+'\n')
	tn.write('conf t'.encode()+'\n')
	tn.write('router ospf 1'.encode()+'\n')
	tn.write('network 0.0.0.0 0.0.0.0 a 0'.encode()+'\n')
	tn.write(Exit.encode()+'\n')
	tn.write('exit'.encode()+'\n')
        tn.write(CMD.encode()+'\n')
        telreply = tn.expect([],timeout=1)[2].decode().strip()
        DeviceName = re.search('.*(?=#show run)',telreply).group()
        tn.close()
	log = open(DeviceName + '-' + LogTime + '.txt','w')
	log.write(telreply)
	log.close()
