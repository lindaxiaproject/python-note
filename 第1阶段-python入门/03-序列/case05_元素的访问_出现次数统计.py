"""
    列表元素访问和计数
    index()获得指定元素在列表中首次出现的索引
    count()获得指定元素在列表中出现的次数
    len()返回列表长度
    成员资格判断--in 关键字来判断，直接返回 True 或 False
"""
a = [10,20,30,40,50,20,30,20,30]
# 30
print(a[2])
# IndexError: list index out of range
# print(a[9])

# 元素在列表中首次出现的索引为：1
print(a.index(20))
# 从索引位置3开始往后搜索的第一个20 元素在列表中出现的索引为：5
print(a.index(20,3))
# 从索引位置5到7这个区间，第一次出现30元素的位置 元素在列表中出现的索引为：6
print(a.index(30,5,7))

aa = [10, 20, 30, 40, 50, 20, 30, 20, 30]
bb = aa.count(20)
# 出现的次数：3
print(bb)

aaa = [10,20,30]
# 长度：3
print(len(aaa))


aaaa =  [10,20,30,40,50,20,30,20,30]
# True
print(20 in aaaa)
# False
print(666 in aaaa)