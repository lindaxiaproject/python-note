"""
    Python对于类的成员没有严格的访问控制限制，这与其他面向对象 语言有区别。关于私有属性和私有方法，有如下要点：
        1.通常我们约定，两个下划线开头的属性是私有的(private)。其他为公共的(public)。
        2.类内部可以访问私有属性(方法)
        3.类外部不能直接访问私有属性(方法)
        4.类外部可以通过 _类名__私有属性(方法)名 ”访问私有属性(方法)

"""


# 测试私有属性、私有方法
class Employee:
    # 私有，通过dir查到_Emloyee_company
    __company = "林大侠科技"  # '''解释器运行时，把__company转成了_Employee__company'''

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有实例属性

    def say_company(self):
        print("我的公司是：", Employee.__company)  # 类内部可以直接访问私有属性
        print("我的年龄是：", self.__age)

    def __work(self):
        print("好好工作，好好赚钱！")


# 报错：AttributeError: type object 'Employee' has no attribute '__company'
# print(Employee.__company)
# print(dir(Employee))
# 林大侠科技
# print(Employee._Employee__company)
a = Employee("kkk",19)
a.say_company()
a._Employee__work()

# AttributeError: 'Employee' object has no attribute '__work'
#a.__work()

