"""
    生成器表达式很简单，只要把一个列表推导式的[]改成{},就创建了1个生成器（generator）
"""
L = [x * x for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(L)


g = (x * x for x in range(10))
# <generator object <genexpr> at 0x102a49d20>
print(g)