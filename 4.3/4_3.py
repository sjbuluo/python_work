# -*- coding: utf-8 -*-

for num in range(1,21):
	print(num)
	
import time 	

start = time.time()	

for num in range(1,1000000):
	print(num)
	
end = time.time()

print('take %f seconds' % (end - start))


