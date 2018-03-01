magicians = ['A','B','C','D','E','F']

def show_magicians(m):
	for n in m:
		print(n)

show_magicians(magicians)
		
def make_great(m):
	for i in range(len(m)):
		m[i] = 'The Great ' + m[i]

make_great(magicians)
show_magicians(magicians)
make_great(magicians[:])
show_magicians(magicians)

