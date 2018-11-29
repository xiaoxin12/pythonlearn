print(' sqq is a good boy')

#  输出时间下一秒
timeStr = input()
timeList = timeStr.split(':')
hour = int(timeList[0])
min = int(timeList[1])
sec = int(timeList[2])
sec += 1
if sec == 60:
    min +=1
    sec = 0
    if min ==60:
        hour +=1
        min = 0
        if hour ==24:
            hour = 0
print('%d: %d:%d' % (hour, min, sec))