"""
    继承让我们更加容易实现类 的扩展。实现代码的重用，不用再重新发明轮子(don’t reinvent wheels)。

    Python支持多重继承，一个子类可以继承多个父类。继承的语法格 式如下：
        class  子类类名(父类1[，父类2， ...])：
            类体

    如果在类定义中没有指定父类，则默认父类是object类。也就是object说是所有类的父类，里面定义了一些所有类共有的默认
实现,比如 __new__()

    构造函数
        子类不重写  __init__  ，实例化子类时，会自动调用父类定义的__init__
        子类重写了 __init__  时，实例化子类，就不会调用父类已经定义的
        如果重写了 __init__  时，要使用父类的构造方法，可以使用super关键字，也可以使用如下格式 调用：父类名.__init__(self, 参数列表)

"""
class Person:
    def __init__(self, name, age):
        print("Person的构造方法")
        self.name = name
        self.age = age

    def say_age(self):
        print(self.name,"的年龄是：", self.age())

# Student继承了Person类
class Student(Person):
    def __init__(self, name, age , score):
        # 子类并不会自动调用父类的__init__()，我 们必须显式的调用它。
        # 方式1： Person.__int__(self, name, age)
        super(Student, self).__init__(name, age)
        print("Student的构造方法")
        self.score = score
'''
    Person的父类是obejct类
    Student类的父类是Person类，拥有name、age、score属性、用于say_age方法
    

    Person的构造方法
    Student的构造方法
    [.....'__weakref__', 'say_age', 'score']
'''
s1 = Student("林大侠", 18, 119)
print(dir(s1))