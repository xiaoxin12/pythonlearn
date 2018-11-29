# -*- coding: utf-8 -*-

count = 0
space = 100
def personCount(name,age=20,city='xian'):
	global count; global space
	count += 1
	space -= 1
	print(name)
	print(count)
	print('剩余空间',space)
personCount('xiaoming')
personCount('ming')
personCount('贺丽霞')
personCount('于大头')