

Person = type('Person', (), {})
# 是否可以用Person创建对象
p1 = Person()
# <__main__.Person object at 0x100baf2e0>
print(p1)
# [<class '__main__.Person'>, <class 'object'>]
print(Person.mro())

class Animal():
    def __init__(self, color):
        self.color = color
    def eat(self):
        print("动物需要吃东西")

def sleep(self):
        print("动物需要睡觉")
# 使用type动态创建一个类，父类就是Animal
Dog = type('Dog',(Animal,),{'age':3,'sleep':sleep})
dog = Dog('Yellow')
print(dog.age)
# 动物需要睡觉
dog.sleep()
# 继承了父类中特性 （属性）
print(dog.color)
dog.eat()
print(Dog.__name__)
