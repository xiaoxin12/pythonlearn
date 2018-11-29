import time
musicLrc ="""
[00:03:00]奈何
[00:05:00]作词：琼瑶 作曲：徐嘉良
[00:23:12]我和你两个
[00:24:79]伴着灯儿坐
[00:29:60]我低头无语
[00:32:78]你眉头深锁
[00:37:06]好花好月好良宵
[00:40:69]它不属于你
[00:44:15]也不属于我
[00:51:86][02:19:29]心事几万重
[00:53:77][02:21:26]只有情默默
[00:58:35][02:25:75]想对灯儿说
[01:01:56][02:28:99]灯儿不解我
[01:06:31][02:33:50]好花好月好良宵
[01:09:74][02:37:05]如此虚度过
[01:13:37][02:40:69]泪珠悄悄落
[01:21:10][02:48:61]错错错
[01:24:25][02:51:66]一路走来是谁错
[01:28:15][02:55:86]这这这
[01:31:35][02:58:71]这份愁肠如何说
[01:35:56][03:02:72]好花好月好良宵
[01:38:86][03:05:92]你也是奈何
[01:40:77][03:07:99]我也奈何
[01:42:99][03:10:36] 奈何 奈何 奈何 奈何……
"""
#  按行怼歌词进行拆分
musicLrcList = musicLrc.splitlines()
# print(musicLrcList)
lrcDict = {}
for lrcLine in  musicLrcList :
    # runCount = Lrcline.count(':')
    LrclineList = lrcLine.split("]")
    # print(LrclineList[-1])
    for index in range(len(LrclineList) - 1 ):
        timeStr = LrclineList[index][1:]
        # print(timeStr)
        timeList = timeStr.split(':')
        time1 = float(timeList[0])*60 + float(timeList[1])
        # print(time)
        lrcDict[time1] = LrclineList[-1]

print(lrcDict)
allTimeList = []
for t  in lrcDict:
    allTimeList.append(t)
allTimeList.sort()

print(allTimeList)
"""
while 2:
    getTime = float(input('请输入一个时间：'))
    # print(len(allTimeList))
    for n in range(len(allTimeList)):
        tempTime = allTimeList[n]
        if getTime < tempTime:
            break
    if n == 0:
        print('时间太小')
    else:
        print(lrcDict[allTimeList[n - 1]])
"""
getTiem = 0
while 1:
    for n in range(len(allTimeList)):
        tempTime = allTimeList[n]
        if getTiem < tempTime:
            break
    lrc = lrcDict.get(allTimeList[n-1])
    if lrc == None:
        pass
    else:
        print(lrc)
    time.sleep(0.5)
    getTiem += 3

