# -*- coding: utf-8 -*-

names = ['A','B','C']

print(names)

names.insert(0,'D')
names.insert(0,'E')
names.insert(0,'F')

print(names)

names = ['A','B','C']

names.insert(len(names)//2,'D')
names.insert(len(names)//2,'E')
names.insert(len(names)//2,'F')

print(names)

names = ['A','B','C']

names.append('D')
names.append('E')
names.append('F')

print(names)

while(len(names) > 2):
	print(names.pop())
	
print(names)

while len(names) > 0:
	del names[0]
	
print(names)
