"""
    类方法是从属于“类对象”的方法。类方法通过装饰器@classmethod义，格式如下：

        @classmethod
        def  类方法名(cls  [，形参列表]) ：
            方法体

       （1） @classmethod必须位于方法上面一行
       （2）第一个 cls 必须有； cls 指的就是“类对象”本身
       （3）调用类方法格式：类方法.类方法名(参数列表)。 参数列表中，不需要也不能给 cls 传值类方法中访问实例属性和实例方法会导致错误

"""
class Student:
    company = "kkk" # 类属性
    def __init__(self, name):
        self.name = name

    @classmethod
    def printCompany(cls):
        print(cls.company)

# kkk
Student.printCompany()

"""
    Python中允许定义与“类对象”无关的方法，称为“静态方法”。
    静态方法”和在模块中定义普通函数没有区别，只不过“静态方法”放到了“类的名字空间里面”，需要通过“类调用”。
    静态方法通过装饰器@staticmethod来定义
"""

class Student2:
    company = "kkk" # 类属性
    def __int__(self, name):
        self.name = name

    @classmethod # 类方法
    def printCompany(cls):
        print(cls.company)

    @staticmethod # 静态方法
    def add(a, b):
        print("{0}+{1}={2}".format(a, b ,(a+b)))
        return a+b


Student2.printCompany()
Student2.add(40, 60)