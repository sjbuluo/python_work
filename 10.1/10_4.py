while True:
	name = input('UR Name: ')
	if name == 'quit':
		break
	else:
		with open('guest.txt','a') as f:
			f.write('\n',name)
