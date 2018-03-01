try:
	while True:
		age = int(input('Your age: '))
		if age < 3:
			print('Free')
		elif age < 12:
			print('$10')
		else:
			print('$15')
except BaseException as e:
	print('END')
