"""
  class 类名
    实际上，当解释器执行class语句时，就会创建一个类对象

"""

class Student:
    pass

# <class 'type'> type类型
print(type(Student))
# 4661999072
print(id(Student))
# <class '__main__.Student'>
print(Student)

Stu2 = Student
s1 = Stu2()
# <__main__.Student object at 0x104c3f340>
print(s1)