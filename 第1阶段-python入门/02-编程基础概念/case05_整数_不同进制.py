"""二进制 结果为41"""
a = 0b101001
print(a)
"""八进制 结果为9"""
b = 0o11
print(b)
"""16进制 一个f表示15 结果为255"""
c = 0xff
print(c)

""" 转化为整数类型 输出：9 """
d = int(9.8)
print(d)

""" 
    自动转型 <class 'float'>
"""
e = 10
f = 0.2
print(type(e+f))

""" 计算超大数结果，没有位数限制 """
g = 10 ** 1000
print(g)