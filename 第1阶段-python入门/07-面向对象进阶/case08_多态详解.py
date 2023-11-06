"""
    多态（polymorphism）是指同一个方法调用由于对象不同可能会 产生不同的行为。

      多态是方法的多态，属性没有多态。
      多态的存在有2个必要条件：继承、方法重写
"""

class Animal:
    print("动物叫了一声")

class Dog(Animal):
    def shout(self):
         print("小狗，汪汪汪")

class Cat(Animal):  # 方法继承
    def shout(self): # 方法重写
        print("小猫，喵喵喵")

def animalShout(a):
     a.shout()  # 传入的对象不同， shout方法对应的实际行为也不同。

"""
动物叫了一声
小狗，汪汪汪
小猫，喵喵喵
"""
animalShout(Dog())
animalShout(Cat())