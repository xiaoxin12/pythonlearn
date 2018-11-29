# !/usr/bin/python

# _*_ coding:UTF-8_*_

# 计算几个数字中间的最小数
numList = []
def inputc(sr):
    count= input(sr)
    if count == '':
        print('输入内容不能为空，您必须输入一个数字')
        inputc(sr)
    else:
        return count
for i in range(0, 3):
    sr = '请输入第'+str(i+1)+'个数:'
    c = inputc(sr)
    try:
        x = int(c)
        numList.append(x)
    except:
        print('输入内容必须是数字')

numList.sort()
print('在输入的数字集合', numList, '中最小的数字是：', numList[0])

print(max(numList), min(numList))
