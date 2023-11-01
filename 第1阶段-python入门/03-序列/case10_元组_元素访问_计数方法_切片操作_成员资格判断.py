"""
    元组的元素访问和计数
        元组的元素不能修改
        元组的元素访问、index()、count()、切片等操作，和列表一 样。
"""
a = (20, 10, 30, 9, 8)
# a[3] = 33
# TypeError: 'tuple' object does not support item assignment
# print(a)


b = (20, 10, 30, 9, 8)
# 10
print(b[1])
# (10, 30)
print(b[1:3])
# (20, 10, 30, 9)
print(b[:4])

c = (20,10,30,9,8)
d = sorted(c)
# [8, 9, 10, 20, 30]
print(d)

"""
    zip(列表1，列表2， ...)将多个列表对应位置的元素组合成为元组，并返回这个zip对象。
"""
aa = [10,20,30]
bb = [40,50,60]
cc = [70,80,90,100]
dd = zip(aa,bb,cc)
# <zip object at 0x102a75500>
print(dd)
ee = list(dd)
# [(10, 40, 70), (20, 50, 80), (30, 60, 90)]
print(ee)
