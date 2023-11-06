"""
    Python对象中包含了很多双下划线开始和结束的属性，这些是特殊 属性，有特殊用法。
    obj.__dict__ 对象的属性字典
    obj.__class__  对象所属的类
    class.__bases__  表示类的父类(多继承时，多个父类放到一个元组中)
    class.__base   类的父类
    class.__mro __ 类层次结构
    class.__subclasses__()  子类列表
"""

class A:
    pass
class B:
    pass
class C(B,A):
    def __init__(self,nn):
        self.nn = nn
    def cc(self):
        print("cc")
'''
    {'nn': 3}
    <class '__main__.C'>
    (<class '__main__.B'>, <class '__main__.A'>)
    [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
    [<class '__main__.C'>]
'''
c = C(3)
print(c.__dict__)
print(c.__class__)
print(C.__bases__)
print(C.mro())
print(A.__subclasses__())