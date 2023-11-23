from functools import reduce
"""
    在一个list中，删掉偶数，只保留奇数
"""

def is_odd(n):
    return n % 2 ==1

L = filter(is_odd,[1, 2, 4, 5])
# [1, 5]
print(list(L))
"""
    用匿名函数实现
"""
L2 = filter(lambda n:n%2==1,[1,2,3,4,5])
# [1, 3, 5]
print(list(L2))
"""
    filter序列中的空字符串删掉
"""
def not_empty(s):
    return s and s.strip()
L3 = filter(not_empty,['A','','B',None,'C', '   '])
# ['A', 'B', 'C']
print(list(L3))
"""
    用匿名函数实现
"""
L4 = filter(lambda s:(s and s.strip()),['A','','B',None,'C', '   '])
print(list(L4))

