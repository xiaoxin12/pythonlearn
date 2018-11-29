# !/usr/bon/python
# _*_ coding: UTF-8 _*_

# for x in range(100, 1000):
#     # c = str(x)
#     # b = int(c[0])
#     # s = int(c[1])
#     # g = int(c[2])
#     b = x // 100
#     s = x // 10 % 10
#     g = x % 10
#     # print(b,s,g)
#     if x == b**3 + s**3 + g**3:
#         print(x)

# 递归打印所有的水仙花数
def shuixian(n = 0, m = 1000):
    total = 0
    for x in range(n, m):
        c = str(x)
        c2 = 0
        # print(len(c))
        for i in range(0, len(c)):
            c2 = c2 + (int(c[i]) ** len(c))
        if x == c2:
            total += 1
            print(x)
    print('从%s到%s 之间总共有%s 个水仙花数' % (n, m, total))
shuixian(0,100000)

print([i for i in range(100,1000) if (i//100)**3+((i-i//100*100)//10)**3+(i%10)**3 == i])
print(list(i for i in range(100,1000) if (i//100)**3+((i-i//100*100)//10)**3+(i%10)**3 == i))