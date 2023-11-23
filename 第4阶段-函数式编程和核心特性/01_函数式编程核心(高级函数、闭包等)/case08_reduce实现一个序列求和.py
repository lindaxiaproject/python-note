from functools import reduce
"""
    reduce实现对一个序列求和
"""

def add(x, y):
    return x+y
sum = reduce(add, [1,3,5,7,9])
# 25
print(sum)