from functools import cmp_to_key


class Student:
    def __init__(self, age, name):
        self.name = name
        self.age = age

def custom_sorted(stu1, stu2):
    if stu1.age > stu2.age:
        return 1
    elif stu1.age < stu2.age:
        return -1
    else:
        return 0

s1 = Student(20, "John")
s2 = Student(10, "lindaxia")
s3 = Student(30, "tomcat")

# Student_list = sorted([s1, s2, s3], key=lambda  x: x.age)
Student_list = sorted([s1, s2, s3],key=cmp_to_key(custom_sorted))
for stu in Student_list:
    '''
    lindaxia--10
    John--20
    tomcat--30
    '''
    print(f"{stu.name}--{stu.age}")
