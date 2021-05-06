#!/usr/bin/python
import telnetlib
import time
import re
LogTime = time.strftime('%Y-%m-%d')
for line in open("cisco_ip_list.txt"):
	Host = line
	CMD = 'show run'
    UserName = 'cisco'
    PassWord = 'cisco'
	tn = telnetlib.Telnet(Host)
    F = tn.read_until('No route to host')
	f = 'No route to host'
                #f = 'No route to host'
                #F = tn.read_until('No route to host')
	if f == F :
		print line
	else：
		tn.write(UserName.encode())
		tn.write(b'\n')
		tn.write(PassWord.encode())
		tn.write(b'\n')
		tn.write('enable'.encode())
		tn.write(b'\n')
		tn.write('ccie'.encode())
		tn.write(b'\n')
		tn.write('terminal length 0'.encode())
		tn.write(b'\n')
		tn.write(CMD.encode())
		tn.write(b'\n')
		telreply = tn.expect([],timeout=1)[2].decode().strip()
		DeviceName = re.search('.*(?=#show run)',telreply).group()
		tn.close()