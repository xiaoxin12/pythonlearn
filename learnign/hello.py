# print('hello world')
# print(100+300);
# # name = input()
# # print(name);
# #!/usr/bin/python
# names =input('please enter your name: ')
# print ('hello,', names)
# print(ord(names))
# print(chr(ord(names)))
# -*- coding: utf-8 -*-
# strs = 'hello,小明去年的成绩是 {0}今年的成绩是 {1}提升了  {2:.2f}%'.format(78,90,((90-78)/78*100))
# str1 = input('小明去年的成绩是:')
# str2 = input('小明今年的成绩是:')
# c = (str2-str1)/str1*100
# print(c)
# print('小明的成绩提升饿了{0:.1f}%'.format(c))

# 以下代码即将实现数组的功能
# arr = ['xiaom', 'xiaon', 'xiaoc']
# print(arr)
# print(arr[len(arr)-1])
# print(arr.pop(len(arr)-1))
# print(len(arr));
# print(arr)


# ints1 = input('请输入一个数字：')
# ints = int(ints1)
# # if ints>=10:
# # 	print('你输入的数字比10大')
# # 	pass
# # else :
# # 	print('你输入了什末,',ints)
# arr = list(range(ints));
# sum = 0;
# for x in arr:
# 	sum = sum +x
# print(sum)
# account = 10000
# while sum>100:
# 	sum = sum-1
# 	account = account-sum
# print(account)

# 这里进行其他的一些工作开发例如dist和set
# d = {"hello":90,"cello":80}
# print(d['hello'])
# d['hello'] = 100
# print(d)
# if 'hells' in d:
# 	print(d['hello'])
# elif 'hello' in d:
# 	d.pop('hello')
# print(d.get('hello','false'))

# s= set([1,'1',1,2,2,3,4])


# 实现任意数字的求和功能
# print('求从数字X到数字Y之间所有数字的和')
# nums1 = input('请输入一个数字X：')
# nums2 = input('请输入一个数字Y：')
# num1 = int(nums1)
# num2 = int(nums2)
# def sums1(x,y):
# 	s= 0
# 	if y == x:
# 		s = 0
# 	while y>x:
# 		y = y -1
# 		if y==x:
# 			y = 0
# 		s = s + y

# 	return s
# def sums2(x,y):
# 	s= 0
# 	if y==x:
# 		s = 0
# 	while y>x:
# 		s = s + y
# 		y = y -1
# 		if y == x:
# 			s = s + y
# 	return s
# print('从',num1,'到',num2,'之间所有数字的和（不包含X和Y）是',sums1(num1,num2) )
# print('从',num1,'到',num2,'之间所有数字的和（包含X和Y）是',sums2(num1,num2) )


# 递归求阶乘
# def  fect(n , prodect):
# 	if n==1:
# 		return 1
# 	if n==0:
# 		return 1
# 	return fect(n-1,n*prodect)
# n = input('请输入一个数字n:')
# n2 = input('请输入一个数字最下之:')
# n = int(n)
# n2 = int(n2)
# print(fect(n,n2))

#  汉诺塔
def hannuota(n,a,b,c):
	if n==1:
		print ('move',a,'--->',c)
	else:
		hannuota(n-1,a,c,b)
		hannuota(1,a,b,c)
		hannuota(n-1,b,a,c)

# print(hannuota(n ,'A',"B","C"))

# 获取数组种的非字符串内容

lists = ['Hello', 'World', 18, 'Apple', None]
b=[s.lower() for s in lists if isinstance(s,str)]
print(b)