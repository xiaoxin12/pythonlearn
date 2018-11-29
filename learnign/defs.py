def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax +n
	return ax

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
f = lazy_sum(1,2,3,4,5,6)
# print(f())
# print(f)

def count():
	fs = []
	def f(x):
		def g():
			return x*x
		return g
	for x in range(1,4):
		fs.append(f(x))
	return fs
f1,f2,f3 = count()

def log(func):
	def wrapper(*args,**kw):
		print('call %s():', % func._name_)
		return func(*args,**kw)
	return wrapper
@log
def now():
	print('2015-3-25')
# print(now())

