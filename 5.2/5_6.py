try:
	age = int(input())
	if age < 2:
		print('<2')
	elif age < 4:
		print('>2 and <4')
	elif age < 13:
		print('>4 and <13')
	elif age < 20:
		print('>13 and <20')
	elif age < 65:
		print('>20 and <65')
	else:
		print('>65')
except BaseException as e:
	print(e)
