#  _*_ coding:utf-8 _*_

# 注释：
# 多行注释可以用多个# 号还有'''或者"""
# 应用缩进来表示代码块不需要使用{}
# 通常一行写完一个语句，但是语句如果比较长可以使用反斜杠\来实现
# 在[]、{}或者()中的多行语句。无需使用反斜杠
# 常见四种数字类型：int(整数)、bool(布尔)、float(浮点数)、complex（复数）


#！/usr/bin/python3
str = "have a pig"
# print(str[0:-1],'have a pi')
# print(str[0],'h')
# print(str[2:8],'ve a pi')
# print(str[2:],'ve a pig')
# print(str*2,'have a pighave a pig')
# print('hello\na pig')
# print(r'hello\na pig')

# 等待用户输入
# input('\n\n 按下enter 后退出')


# 同一可以显示多条语句
# import sys; x = 'runoob'; sys.stdout.write(x + '\n')


# 数字运算符
a = 10.101
b = -20
import math
print(abs(b),20)
print(math.fabs(b),20.0)
print(math.floor(a),10)
print( math.ceil(4.1) )
print( ( (a>b) - (a<b) ) ,1 )
print( math.exp(a) , '有点难' )
print( math.log(math.e) , '1.0' )
print( math.log(100,10) , '2.0' )
print( math.log(1300,10) , '??' )
print(max(10,20,3,0,30,65,9))
print(math.modf(9.22))
print(round(9.22  ,1))
print(math.pow(a,b) )

