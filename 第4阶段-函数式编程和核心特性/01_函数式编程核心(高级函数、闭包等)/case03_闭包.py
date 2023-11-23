

"""
    闭包特点：
        1.存在内外层函数嵌套的情况
        2.内层函数引用了外层函数的变量或参数（自由变量）
        3.外层函数把内层的这个函数本身当作返回值进行访问
    outer
    -------
    inner
    a:1
"""
def outer():
    print("outer")
    a =1
    def inner():
        print("inner")
        # 闭包是由于函数内部使用了函数外部的变量，这个函数对象不销毁，则外部函数的局部变量也不会销毁
        nonlocal  a
        print(f"a:{a}")
        a += 1
    return inner
a = outer()
print("-------")
a()
