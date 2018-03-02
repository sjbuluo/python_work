content = ''

with open('learning_python.txt','r') as f:
	content = f.read()
	
from os import path 

if path.exists('learning_c.txt'):
	with open('learning_c.txt','w') as f:
		f.write(content.replace('python','C'))
else:
	with open('learning_c.txt','x') as f:
		f.write(content.replace('python','C'))
