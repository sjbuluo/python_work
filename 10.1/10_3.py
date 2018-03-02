name = input('UR Name: ')

with open('guest.txt','w') as f:
	f.write(name)
