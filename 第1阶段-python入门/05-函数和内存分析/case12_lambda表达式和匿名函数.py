"""

    lambda表达式可以用来声明匿名函数。
        lambda 函数是一种简单的、在同一行中定义函数的方法。
         lambda函数实际生成了一个函数对象。表达式只允许包含一个表达式，不能包含复杂语句，该表达式的计算结果就是函数的返回值。

     基本语法： lambda  arg1,arg2,arg3...  :  <表达式>
"""

f = lambda a, b, c: a + b + c

# <function <lambda> at 0x100787e20>
print(f)
# 60
print(f(10, 20, 30))
# <class 'function'>
print(type(f))


g = [lambda a:a*2, lambda b:b*3, lambda c:c*3]
# [<function <lambda> at 0x1052848b0>, <function <lambda> at 0x105284b80>, <function <lambda> at 0x105287c70>]
print(g)
# 12
print(g[0](6))
# 12 21 16
print(g[0](6), g[1](7), g[0](8))
