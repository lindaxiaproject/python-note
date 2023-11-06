"""
    __del__方法 (析构函数)和垃圾回收机制
    （1）__del__方法
        1.1.__del__() 称为“析构方法”，用于实现对象被销毁时所需的操作。
            比如：释放对象占用的资源，例如：打开的文件资源、网络连接等。
        1.2.Python实现自动的垃圾回收，当对象没有被引用时（引用计数为 0），由垃圾回收器调用 __del__()
        1.3.可以通过 del语句 删除对象，从而保证调用 __del__()
"""

class Person:
    def __del__(self):
        print("销毁对象：{0}".format(self))

"""
    销毁对象：<__main__.Person object at 0x10114b340>
    程序结束
    销毁对象：<__main__.Person object at 0x10114beb0>
"""
p1 = Person()
p2 = Person()
del p2
print("程序结束")