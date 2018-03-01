names = ['admin','A','C','E','F','D']

if names:
	for name in names:
		if 'admin' == name:
			print('Hello admin, would you like to see a status report?')
		else:
			print('Hello %s, thank you for logging in again' % name)

while names:
	names.pop()
	
if names: 
	pass
else:
	print('no names')
