import functools


"""
     base参数
"""
# 转换为八进制 5349
print('转换为八进制', int('12345', base =8))

int2 = functools.partial(int, base=2)
print(int2('1000000'))  # 64
print(int2('1010101'))  # 85