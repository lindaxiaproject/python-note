"""
    Python的运算符实际上是通过调用对象的特殊方法实现的。
        __init__ :构造方法
        __del__ :析构方法
        __repr__、__str__:打印，转换
        __call__:函数调用
        __getattr__: 点号运算
        .....
    每个运算符实际上都对应了相应的方法
"""

a = 20
b = 30
c = a+b
d = a.__add__(b) # 本质解释器会调用".__add__"方法
print("c=",c)  # c= 50
print("d=",d) # d= 50

class Person:
    def __init__(self,name):
        self.name = name

    def __add__(self, other):
        if isinstance(other,Person):
            return "{0}--{1}".format(self.name,other.name)
        else:
            return "不是同类对象，不能相加"
    def __mul__(self, other):
        if isinstance(other,int):
            return  self.name*other
        else:
            return "不是同类对象，不能相乘"

p1 = Person("林大侠")
p2 = Person("牛人")

x = p1+p2
print(x)
print(p1*3)