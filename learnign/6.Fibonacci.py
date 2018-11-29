# !/usr/bin/python
# _*_ coding: UTF-8 _*_

#题目：斐波那契数列。

# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
#
# 在数学上，费波那契数列是以递归的方法来定义：

# F0 = 0     (n=0)
# F1 = 1    (n=1)
# Fn = F[n-1]+ F[n-2](n=>2)
# 这里是以多种方法组成的
# 方法1 循环
def fibonacci1(n):
    a,b = 1, 1
    if n ==0:
        a = 0
    for i in range(n - 1):
        a, b = b, a + b
    return a
# for n in range(0,11):
#     print(fibonacci1(n))


# 方法2 递归法
def fibonacci2(n):
    if n == 0:
        return 0
    elif (n == 1)or(n == 2):
        return 1
    return fibonacci2(n-1) + fibonacci2(n-2)

#
# for n in range(0, 11):
#     print(n, fibonacci2(n))

# 方法3
def fibonacci3(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    if n == 2:
        return [0, 1, 1]
    fibs = [0, 1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs
for n in range(0, 11):
    print('fibonacci3中n=', n, '输出结果为', fibonacci3(n))





