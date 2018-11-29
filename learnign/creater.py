# -*- coding: utf-8 -*-
# 这是一个python 生成器 generator


# L = [x for x in range(10)]
# K = {x for x in range(10)}
# G = ( x for x in range(100) )

# for i in G:
# 	print(i+1)


def fibla(max):
	n, a, b = 0, 0, 1
	while n<max:
		print(b)
		a,b = b ,a+b
		n= n+1
	return '第一次执行玩了'
# 下面的函数执行后不会得到任何的返回
def fibla2(max):
	n, a, b = 0, 0, 1
	while n<max:
		yield b
		a,b = b ,a+b
		n= n+1
	return '执行玩了'
# 用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
# n=fibla2(15)
# while True:
# 	try:
# 		x = next(n)
# 		print('fibla2:',x)
# 	except StopIteration as e:
# 		print(e.value)
# 		break

#  杨辉三角
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：

# 行数索引为 0 ，打印1 
# 行数索引为1 ，打印1 ，1 
# 行数索引为2 打印1，2，2
# 行数索引为3 打印1，3，3， 1
# 行数索引为4 打印1，4，6，4，1
# 行数索引为5 打印1，5，10 ，10 ，5，1
# 规律总结 每行元素个数为N+1 个，元素内容

# def triangles():
#     a=[1]
#     while True:
#         yield a
#         a=[sum(i) for i in zip([0]+a,a+[0])]
# n = 0
# for t in triangles():
#     print(t)
#     n=n+1
#     if n == 10:
#         break

def yangHuiTrangles():
	l = [1]
	while True:
		yield l
		l.append(0)
		l = [ l[i-1]+l[i] for i in range(0,len(l)) ]
n = 1
for v in yangHuiTrangles():
	print(v)
	n = n+1
	if n == 6:
		break 
