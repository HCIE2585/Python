
#!/usr/bin/evn python
while True:
	input=raw_input("Please input username:")
	if input == 'cisco':
		password=raw_input("Please input password:")
		p = 'cisco'
		while password != p:
			password=raw_input("Wrong passwd,input again:")
		else:
			print 'Welcome Login !\n'
			break
	else:
		print "Sorry,username %s not found" % input