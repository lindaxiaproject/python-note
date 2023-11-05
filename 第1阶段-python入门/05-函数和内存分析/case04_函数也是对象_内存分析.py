"""
    Python中，“一切都是对象”。

    实际上，执行 def 定义函数后，系统就 创建了相应的函数对象。
"""

def print_star(n):
    print('*'*n)

# <function print_star at 0x1011b3e20>
print(print_star)
# 4371889696
print(id(print_star))
# ***
c = print_star(3)

d = print_star
d(3)


zhengshu = int
# 1234
print(zhengshu("1234"))

s = str
# 333
print(s(333))

