t = (1,2,3,4,5)

for x in t:
	print(x)
	
#t[1] = 6

def add_tuple(old,add):
	l = []
	for x in old:
		l.append(x)
	for x in add:
		l.append(x)
	return tuple(l)
	
print(add_tuple(t, (8,9)))
