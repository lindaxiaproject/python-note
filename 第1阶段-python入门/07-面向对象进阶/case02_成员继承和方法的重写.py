"""
    成员继承：子类继承了父类除构造方法之外的所有成员。(私有属性、私有方法也被继承)
    方法重写：子类可以重新定义父类中的方法，这样就会覆盖父类的方法，也称为“重写”
"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say_age(self):
        print(self.name,"的年龄是： ",self.age)
    def say_name(self):
        print("我是",self.name)

class Student(Person):
    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        self.score = score

    def say_score(self):
        print(self.name, "的分数是： ",self.score)

    # 重写父类的方法
    def say_name(self):
        print("报告老师，我是", self.name)

'''
张三 的分数是：  85
报告老师，我是 张三
张三 的年龄是：  15
'''
s1 = Student("张三",15,85)
s1.say_score()
s1.say_name()
s1.say_age()


"""
   通过类的方法mro()或者类的属性__mro__可以输出这个类的继承层次结构。 
   [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
   c继承B,B继承A
"""
class A:pass
class B(A):pass
class C(B):pass
print(C.mro())
