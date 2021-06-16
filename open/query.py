#!/usr/bin/evn python
while True:
	input=input("input your name:")
	if input == "cisco":
		password=input("input your password:")
		p='cisco'
		while password != p:
			password=input("try again:")
		else:
			print('welcome longin to System')
			while True:
				match_yes = 0
				input=input("please input search name:")
				contact_file=file("list.txt")
				while True:
					line= contact_file.readline()
					if len(line)==0:break
					if input in line:
						print'Match item:' % line
						match_yes = 1
					else:
						pass
					if  match_yes == 0:
						print'No match item found'			
	else:
		print"Sorry,user %s not found" % input
				
		
		

	
	
