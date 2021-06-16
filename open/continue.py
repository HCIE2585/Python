while True:
	s = input('please enter:')
	if len(s) == 5:
		break
	if len(s) > 5:
		print ('Too long!')
		continue
	else:
		print ('Too short!')
print ('Thanks a million')