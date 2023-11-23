# coding=utf-8
import types


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("lindaxia", 20)
p2 = Person("tom", 30)
# 动态给对象添加属性和方法
p1.score = 100
print(p1.score)


def run(self):
    print(f"{self.name},running...")


# 动态的对象添加方法
p1.run = types.MethodType(run, p1)
p1.run()
