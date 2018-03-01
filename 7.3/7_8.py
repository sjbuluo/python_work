sandwich_orders = [1,2,3,4,5,6,7,8,9]

finished_sandwiches = []

import time

while sandwich_orders:
	time.sleep(1)
	t = sandwich_orders.pop(0)
	print('I made your', t)
	finished_sandwiches.append(t)
	
print(finished_sandwiches)
