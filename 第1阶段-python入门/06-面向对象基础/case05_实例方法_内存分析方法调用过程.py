"""
    实例方法是从属于实例对象的方法。实例方法的定义格式如下
        def  方法名(self [, 形参列表])：
            函数体
    定义实例方法时，第一个参数必须为 self  。和前面一样，self 指当前的实例对象。
    调用实例方法时，不需要也不能给self 传参。self由解释器自动传参

    dir(obj)：可以获得对象的所有属性、方法
    obj.__dict__  ： 对象的属性字典
    pass： 空语句
    isinstance（对象,类型): 判断“对象”是不是“指定类型”
"""

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def say_score(self, c):
        self.age = 18
        print(c)
        print("{0}的分数是{1}".format(self.name, self.score))

a = Student("林大侠", 18)
a.say_score(68)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'age', 'name', 'say_score', 'score']
print(dir(a))
# {'name': '林大侠', 'score': 18, 'age': 18}  对象的属性字典
print(a.__dict__)
# True
print(isinstance(a, Student))