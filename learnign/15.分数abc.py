# !/usr/bon/python
# _*_ coding: UTF-8 _*_



score = input('请输入一个成绩')

try:
    score = int(score)
except SyntaxError:
    print(SyntaxError)
except BaseException:
    print('请输入正确的成绩')
    print('str(Exception):\t', str(BaseException))
except:
    print('请输入正确的成绩')





