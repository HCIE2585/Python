while True:
	s = input('Please Enter String:')
	if len(s) == 5:
		break
	if len(s) > 5:
		print ('Too long!')
		continue
	else:
		print ('Too short!')
print ('Thanks a million')