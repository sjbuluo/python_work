l = []

while True:
	message = input('Something: ')
	if message == 'quit':
		break
	else:
		print('Add', message)
		l.append(message)

print(l)
