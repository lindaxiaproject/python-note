"""
    实例属性是从属于实例对象的属性，也称为"实例变量"。
        实例属性一般在__init__()方法中通过代码定义： self.实例属性名 = 初始值
        在本类的其它实例方法中，也是通过self进行访问： self.实例属性名
        创建实例对象后，通过实例对象访问：
            obj01 = 类名()        //创建和初始化对象，调用__int__()舒适化属性
            obj01.实例属性名 = 值  // 可以给已有属性赋值，也可以新加属性

"""

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def say_score(self):
        self.age = 18
        print("{0}的分数是{1}".format(self.name, self.score))

'''
    林大侠的分数是99
    18
'''
s1 = Student("林大侠", 99)
s1.say_score()
print(s1.age)
# s1对象增加salary属性
s1.salary = 3000

'''
    林二侠的分数是18
    18
'''
s2 = Student("林二侠", 18)
s2.say_score()
print(s2.age)

