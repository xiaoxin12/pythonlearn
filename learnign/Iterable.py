from collections import Iterable
# print (isinstance( [], Iterable))
# print (isinstance( {}, Iterable))
# print (isinstance( (1,), Iterable))
# print (isinstance( 'asdf', Iterable))
# print (isinstance( 20, Iterable))

def f(x):
	return x*x
r = map(f,[1,2,3,4,5,6,7,8,9])
# print(list(r))
# 引入函数reduce
from functools import reduce 
def add(x,y):
	return x+y
t = reduce(add ,[1,3,5,6,7,8])
# print(t)
def account(x,y):
	return x*10+y

y = reduce(account , [1,3,5,6,7,8])
# print(y)
def char2num(s):
	dig = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
	return dig[s]
u = reduce(account , map(char2num,'159648'))
# print(u)
dig = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2int(s):
	def fn(x,y):
		return x * 10 + y
	def char2num(s):
		return dig[s]
	return  reduce(fn , map(char2num ,s))

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
	dig = {"adam":'Adam',"LISA":'Lisa','barT':'Bart'}
	return dig[name]
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))

# print(L2)

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def  prod(L):
	def product(x,y):
		return x * y
	return reduce(product, L)
# print(prod([3, 5, 7, 9]))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
digs = {'123.456':123.456}
def str2float(s):
	def flo(x,y):
		return x * 10 + y
	n = s.index('.')
	l1 = list(map(int, [x for x in s[:n]] ))
	l2 = list(map(int, [x for x in s[n+1:]] ))
	return reduce(flo,l1) + reduce(flo,l2)/10**len(l2)
print( str2float('123.456'))