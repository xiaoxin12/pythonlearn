# !/usr/bon/python
# _*_ coding: UTF-8 _*_

# 暂停一秒输出。
#
# 程序分析：使用 time 模块的 sleep() 函数。
import time
print(time.time(), '返回当前时间的时间戳(1970元年后的浮点秒数)')
time.sleep(2)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))