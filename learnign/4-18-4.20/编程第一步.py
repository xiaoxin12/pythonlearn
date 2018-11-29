#!/usr/bin/python3
#  _*_ coding:utf-8 _*_
# Fibonacci series:斐波那契数列
# 两个元素的总和确定了下一个数

a ,b = 0, 1
while b < 1000:
    # print(b,end=" ，")
    a,b = b, a + b
    # print(a)


def dogages(age=0):
    print(age)
    if age < 0:
        print('你是逗我呢吧！')
    elif age == 1:
        print('相当于14岁的人。')
    elif age == 2:
        print('相当于22岁的人。')
    elif age > 2 :
        human = 22 + (age -2 ) * 5
        print('对应人类年龄：',human)
ages = int(input('请输入你家狗狗的年龄'))
print('\n\n')
dogages(ages)

