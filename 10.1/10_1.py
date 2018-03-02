with open('learning_python.txt','r') as f:
	print(f.read())
	
with open('learning_python.txt','r') as f:
	for line in f:
		print(line.rstrip())
		
lines = []

with open('learning_python.txt','r') as f:
	lines = f.readlines()
	
for line in lines:
	print(line)
