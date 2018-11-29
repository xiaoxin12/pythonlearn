# !/usr/bon/python
# _*_ coding: UTF-8 _*_


# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
count =0
for x in range(101, 200):
    # 首先先把这个输放出来
    # 如果这个输字能被人一一个2 到自己的数字整除，则不是素数
    issu = 0
    for i in range(2, x):
        if x % i == 0:
            issu = 1
    if issu == 0:
        count += 1
        print(x)
print('总共有%s 个素数' % (count))


# L = list(filter(lambda x: x not in set([i for i in range(101,201) for j in range(2,i) if not i%j]), range(101,201)))
# print('一共有{}个素数，这些素数分别是：{}'.format(len(L),L))
