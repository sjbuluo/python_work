# -*- coding: utf-8 -*-

names = ['a','b','c','d','e']

print('Hi: ' + names[0])
print('Hi: ' + names[1])
print('Hi: ' + names[2])
print('Hi: ' + names[3])
print('Hi: ' + names[4])


for name in names:
	print('For Hi: ' + name)
	
list(map(lambda name: print('Lambda Hi: ' + name), names))



