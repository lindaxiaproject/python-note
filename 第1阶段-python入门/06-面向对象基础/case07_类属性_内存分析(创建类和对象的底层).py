"""
    类属性是从属于“类对象”的属性，也称为“类变量”。由于，类属性从属于类对象，可以被所有实例对象共享。
    类属性的定义方式：
        '''
        class  类名：
            类变量名= 初始值
        '''

"""

class Student:
    company = "林大侠" # 类属性
    count = 0 # 类属性

    '''
        构造函数
    '''
    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.count = Student.count + 1

    def say_score(self): # 实例方法
        print('我的公司是：', Student.company)
        print(self.name,'的分数是：', self.score)

'''
    我的公司是： 林大侠
    林大侠 的分数是： 100
    一共创建2个Student对象
'''
s1 = Student("林大侠", 100)
s2 = Student("林二侠", 99)

s1.say_score()
print('一共创建{0}个Student对象'.format(Student.count))
