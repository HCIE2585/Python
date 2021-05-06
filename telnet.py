import telnetlib
import time
import re
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S') 
Host = '192.168.100.130'
CMD = 'show run' 
UserName = 'cisco'
PassWord = 'cisco'
tn = telnetlib.Telnet(Host) 
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
log = open(DeviceName + '-' + LogTime + '.txt','w')
log.write(telreply)
log.close()
