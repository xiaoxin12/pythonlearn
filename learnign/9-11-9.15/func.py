# 关于对函数set 的理解
# 创建set 需要一个list 或者tuple 或者dict 作为输入集合？
# 重复元素在set 中会被自动过滤
# s1 = set([1,2,3,4,5,1,2,3])
# print(s1)
# s2 = set((1,2,2,3,4))
# print(s2)
#
# s3 = set({1:'good',2:'nice'})
#
# print(s3)

#  set   的添加 可以时重复的但是不会有效果
# set 的元素不能是列表，因为列表是可变的
s4 = set([1,2,3])
s4.add(4)
s4.add(4)
s4.add((5,6,7))
print(s4)
