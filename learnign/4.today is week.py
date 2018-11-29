# !/usr/bin/python
# _*_ coding:UTF-8 _*_
import datetime
#输入某年某月某日，判断这一天是这一年的第几天？
def today(date):
    allday = 365
    months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
    year = int(date.strftime('%Y'))
    month = int(date.strftime('%m'))
    data = int(date.strftime('%d'))
    sum = months[month - 1]
    sum = sum + data
    leap = 0
    if (year % 400 == 0) or (year % 4 == 0) or (year % 100 == 0):
        leap = 1
        allday = 366
    if (leap == 1) and (month > 2):
        sum += 1
    print(year, '年', month, '月', data, '日是这一年的第', sum, '天')
    print('%s年%s月%s日是这一年的第%s天,距离%s年01月01 日还有%s天' % (year, month, data, sum, (year+1), (allday-sum)) )

inputdate = input('请输入一个形如2018-11-18的日期:')
try:
    ity = datetime.datetime.strptime(inputdate, '%Y-%m-%d')
    today(ity)
except:
    print("Error: 输入日期错误，请输入一个正确的日期")



