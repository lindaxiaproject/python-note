"""

    @property 可以将一个方法的调用方式变成“属性调用”。
    @property 主要用于帮助我们处理属性的读操作、写操作。
"""

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    #  方法的调用方式变成“属性调用”
    @property
    def salary(self):
        print("薪资是：", self.__salary)
        return  self.__salary

    # 相当于salary属性的setter方法
    @salary.setter
    def salary(self, salary):
        if(0 < salary < 1000000):
            self.__salary = salary
        else:
            print("薪资录入错误！只能是0-1000000之间！")

'''
薪资是： 50000
50000
'''
emp1 = Employee("林大侠", 1999999)
emp1.salary = 50000
print(emp1.salary)