#!/usr/bin/python
number = 20
running = True

while running:
	guess = int(raw_input('enter the number:'))
	if guess == number:
		print 'You are right!'
		running = False
	elif guess < number:
		print 'No, it is a little higher than that!'
	else:
		print 'No, it is a little lower than that'
else:
	print 'The while loop is over!'
print 'Done!'
