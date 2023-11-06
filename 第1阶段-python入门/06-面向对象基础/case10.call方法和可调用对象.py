"""
     Python 中，凡是可以将 () 直接应用到自身并执行，都称为可调 用对象。
     可调用对象包括自定义的函数、  Python 内置函数、以及本节所 讲的实例对象。
     定义了 __call__()  的对象，称为“可调用对象”，即该对象可以像函数一样被调用。
     该方法使得实例对象可以像调用普通函数那样，以“对象名()”的 形式使用。
"""

def f1():
    print("f1")

'''
    <function f1 at 0x100b2be20>
    4306681376
    <class 'function'>
'''
print(f1)
print(id(f1))
print(type(f1))
f1() # 本质也是调用了__call__()方法
# ['__annotations__', '__builtins__', '__call__', '.....
print(dir(f1))


class Car:
    def __call__(self, age, money): # 重新定call方法
        print("call方法")
        print("车龄： {0},金额： {1}".format(age,money))

f2 = Car()
#  #像调用函数那样调用，本质也是调用了__call__()
f2(3, 200000)