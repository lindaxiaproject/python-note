"""

    设计模式是面向对象语言特有的内容，是我们在面临某一类问题时 候固定的做法，
    设计模式有很多种，比较流行的是：  GOF（Goup  Of Four）23种设计模式。

    最常用的模式：工厂模式和单例模式
        工厂模式实现了创建者和调用者的分离，使用专门的工厂类将选择实现类、创建对象进行统一的管理和控制。
"""

class CarFactory:
    def createCar(self,brand):
        if brand == "奔驰":
            return Benz()
        elif brand == "宝马":
            return BMW()
        elif brand == '比亚迪 ':
            return BYD()
        else:
            return "未知品牌，无法创建"

class Benz:
    pass

class BMW:
    pass

class BYD:
    pass

'''
<__main__.Benz object at 0x104feb8b0>
<__main__.BMW object at 0x104d83c40>

'''
factory = CarFactory()
c1 = factory.createCar("奔驰")
c2 = factory.createCar("宝马")
print(c1)
print(c2)

"""
    单例模式（Singleton Pattern）的核心作用是确保一个类只有一个 实例，并且提供一个访问该实例的全局访问点。
    
    单例模式只生成一个实例对象，减少了对系统资源的开销。
    当一个 对象的产生需要比较多的资源，如读取配置文件、产生其他依赖对 象时，可以产生一个“单例对象”，然后永久驻留内存中，从而极大
的降低开销。
"""

class MySingleton:
    __obj = None
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)
        return cls.__obj

    def __init__(self, name):
        if MySingleton.__init_flag:
            print("初始化一个对象")
            self.name = name
            MySingleton.__init_flag = False

'''
初始化一个对象
<__main__.MySingleton object at 0x1029e3d30>
<__main__.MySingleton object at 0x1029e3d30>
'''
a = MySingleton("aa")
print(a)

b = MySingleton("bb")
print(b)