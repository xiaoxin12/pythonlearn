# !/usr/bin/python
# _*_ coding:UTF-8 _*_

# 这里的需求是打印乘法表

for i in range(1, 10):
    for j in range(1, i+1):
        if i == j:
            print("%d*%d=%d" % (j, i, i * j))
            pass
        else:
            print("%d*%d=%d" % (j, i, i * j), end='  ')