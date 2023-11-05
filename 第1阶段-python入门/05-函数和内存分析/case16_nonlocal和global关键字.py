"""
    nonlocal：用来在内部函数中，声明外层的局部变量。
    global：函数内声明全局变量，然后才使用全局变量
"""

# 使用nonlocal声明外层局部变量
a = 100
def outer():
    b = 10
    def inner():
        nonlocal  b         #声明外部函数的局部变量
        print("inner b:",b)
        b = 20

        global a            #声明全局变量
        a = 1000
    inner()
    print("outer b:",b)

'''
    inner b: 10
    outer b: 20
    a： 1000
'''
outer()
print("a：",a)