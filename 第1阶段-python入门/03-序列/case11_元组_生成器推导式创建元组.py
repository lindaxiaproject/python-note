"""
    列表推导式直接生成列表对象，生成器推导式生成的不是列表也不是元组，而是一个生成器对象。
        通过生成器对象，转化成列表或者元组。也可以使用生成器对象的方法进行遍历
        直接作为迭代器对象来使用
"""

# a = [x*2  for  x  in range(5)]
# [0, 2, 4, 6, 8]
# print(a)

a = (x*2  for  x  in range(5))
# <generator object <genexpr> at 0x104971bd0>
print(a)
aa = tuple(a)
# (0, 2, 4, 6, 8)
print(aa)
# () 只能生成1次
aaa= tuple(a)
print(aaa)

b = (x for x in range(3))
# 0
print(b.__next__())
# 1
print(b.__next__())
# 2
print(b.__next__())
# 抛出异常 StopIteration
# print(b.__next__())





