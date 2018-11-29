# -*- coding: utf-8 -*-
import math
import random

random.random()
number = math.ceil( random.random()*20 )

def gucessfun(num):
    global number
    print(num)
    print(number)
    if num > number:
        print('大了大了，再小点')
    if num < number:
        print('小了小了，再大点')

count = 0
nums = 0
#while count < 3:
#    count + = 1
#    nums = int(input('\n请输入你所猜的数字：'))
#    if nums == number:
#        print('恭喜你猜对了')
#        break
#    else:
#        gucessfun(nums)
print(number)
while count < 5:
    nums = int(input('\n请输入你所猜的数字：'))
    if count == 5:
        print('失败了，没机会了')
        break
    if nums == number:
        print('恭喜你猜对了')
        break
    if nums > number:
        print('大了大了，再小点')
    if nums < number:
        print('小了小了，再大点')
    count += 1


