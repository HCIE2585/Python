#!/usr/bin/python
import telnetlib
import time
import re
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
Host = raw_input('Enter ip address:')
UserName = 'admin'
PassWord = 'passw0rd'
CMD = 'display cur'
tn = telnetlib.Telnet(Host)
tn.read_until('Username:')
tn.write(UserName+'\n')
tn.read_until('Password:')
tn.write(PassWord+'\n')
tn.write(CMD.encode())
tn.write(b'\n')
if:
	tn.read_until(----more----)
	tn.write('\n')
telreply = tn.expect([],timeout=1)[2].decode().strip()
DeviceName = Host
tn.close()
log = open(DeviceName + '-' + LogTime + '.txt','w')
log.write(telreply)
log.close()

