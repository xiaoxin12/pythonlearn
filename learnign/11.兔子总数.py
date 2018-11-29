# !/usr/bon/python
# _*_ coding: UTF-8 _*_

# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
#
# 程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
p1 = 1
p2 = 1

# for i in range(1, 30):
# #     print('%12ld %12ld' % (p1, p2))
# #     if(i % 3) == 0:
# #         print('该多出一对了')
# #     p1 = p1 + p2
# #     p2 = p1 +p2


def rabbyt(n):
    if n == 1 or n == 2:
        return 1
    else:
        return rabbyt(n-1)+ rabbyt(n-2)
for i in range (1,36):
    print(rabbyt(i))