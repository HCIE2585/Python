_author__ = 'Banner'
#!/usr/bin/python
import telnetlib
import time
import re
LogTime = time.strftime('%Y-%m-%d_%H:%M:%S')
Device = raw_input('''Please Select Device
    1:HuaWei;
    2:Cisco;
    3:H3C;
    4:Cisco
Put Device ID:''')
if Device == '1':
        Platform = raw_input('''Please Select Platform :
    1:H3C
    2:H3C
Put Your Choose:''')
        if Platform == '1':
                Protocol= raw_input('''Please Select Platform :
    1:SSH;
    2:Telnet;
Put Your Choose:''')
                if Protocol == '2':
                                for line in open("ip_True.txt"):
                                        Host = line.replace('\n','')
                                        print "Start telnet",Host
                                        UserName = 'admin'
                                        PassWord = 'admin'
                                        tn=telnetlib.Telnet(Host)
                                        tn.write(UserName.encode()+'\n')
                                        tn.write(PassWord.encode()+'\n')
#                                        tn.write('enable'.encode()+'\n')
#                                        tn.write('ccie'.encode()+'\n')
                                        for command in open("H3C-Cmd.txt"):
                                                try:
                                                        cmd = command.replace('\n','')
                                                        tn.write(cmd.encode()+'\n')
                                                        time.sleep(1)
                                                except:
                                                        print cmd,'not found'
                                        telreply = tn.expect([],timeout=1)[2].encode("utf-8")
                                        Hostname = (re.findall(str(".*<(.*)>.*"),telreply))[0]
					tn.close()
					log = open(Host + '-' + LogTime + '.txt','w')
        				log.write(telreply)
        				log.close()
                                        print Host,"Data Collect Successfully!" 
elif Device == '2':
        Platform = raw_input('''Please Select Platform :
        1:Cisco-IOS;
        2:ASA;
Put Your Choose:''')
        if Platform == '1':
                Protocol= raw_input('''Please Select Platform :
        1:SSH;
        2:Telnet;
Put Your Choose:''')
                if Protocol == '2':
                                for line in open("ip_True.txt"):
                                        Host = line.replace('\n','')
					print "Start telnet",Host
                                        UserName = raw_input('''Username:''')
                                        PassWord = raw_input('''Password:''')
					try:
                                        	tn=telnetlib.Telnet(Host)
                                        	tn.write(UserName.encode()+'\n')
                                        	tn.write(PassWord.encode()+'\n')
                                        	tn.write('enable'.encode()+'\n')
                                        	tn.write('ccie'.encode()+'\n')
                                        	for command in open("Cisco-IOS-Cmd.txt"):
                                                        cmd = command.replace('\n','')
                                                        tn.write(cmd.encode()+'\n')
                                                        time.sleep(5)
						telreply = tn.expect([],timeout=1)[2].encode("utf-8")
                                        	Hostname = re.search('.*(?=#show run)',telreply).group()
						tn.close()
        					log = open(Host + '-' + LogTime + '.txt','w')
        					log.write(telreply)
        					log.close()
						print Host,"Data Collect Successfully!"
					except:
                                                print Host,"telnet failed!"       
