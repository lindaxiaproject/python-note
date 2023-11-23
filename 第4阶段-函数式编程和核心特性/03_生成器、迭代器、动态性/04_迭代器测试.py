# #python3.6之前不加.abc，之后的加
from collections.abc import Iterator
from collections.abc import Iterable

a = isinstance([], Iterator)
a = isinstance([], Iterable)
# True
print(a)
""" list 、 dict 、 str 等 Iterable 变成 Iterator , 可以使用 iter() 函数： """
b = isinstance(iter([]), Iterator)
print(b)

c = isinstance(iter('abc'), Iterator)
print(c)
