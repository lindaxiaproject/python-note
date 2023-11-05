"""
    如果函数体中包含return语句，则结束函数执行并返回值
    如果函数体中不包含return语句，则返回None值
    要返回多个值，使用列表、元组、字典、集合将多个值“存起来”即可
"""


# 定义一个打印n个星号的无返回值的函数
def print_star(n):
    print('*' * n)


# **********
print_star(10)


# 定义一个返回两个数平均值的函数
def my_avg(a, b):
    return (a + b) / 2
a1 = my_avg(10, 20) * 100 + 3
# 1503.0
print(a1)

# 返回一个列表
def printShape(n):
    s1 = "#"*n
    s2 = "$"*n
    return [s1,s2]
s = printShape(5)
# ['#####', '$$$$$']
print(s)
# <class 'list'>
print(type(s))
# <class 'function'>
print(type(printShape))
