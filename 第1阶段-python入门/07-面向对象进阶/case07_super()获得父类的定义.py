"""

    在子类中，如果想要获得父类的方法时，我们可以通过super()来做。
    super()代表父类的定义，不是父类对象。
    调用父类的构造方法：super(子类名称,self).__init__(参数列表)
"""

class A:
    def __init__(self):
        print("A的构造方法")
    def say(self):
        print("A: ",self)
        print("say AAA")

class B(A):
    def __init__(self):
        super(B, self).__init__()  # 调用父类的构造方法
        print("B的构造方法")

    def say(self):
        super().say() # 通过super()调用父类的方法
        print("say BBB")

'''
A的构造方法
B的构造方法
A:  <__main__.B object at 0x104836a40>
say AAA
say BBB
'''
b = B()
b.say()