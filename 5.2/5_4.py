# -*- coding: utf-8 -*-

import random

colors = ['G','R','Y']

for x in range(10):
	alien_color = colors[random.randint(0,3)]
	print(alien_color)
	print('5 POINTS' if alien_color == 'G' else 'LOSE')


