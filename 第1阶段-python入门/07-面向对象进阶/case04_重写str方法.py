"""

    obejct方法，用于返回一个__str__对于“对象的描述”。内置函数str(对象)，调用的就是__str__()
	__str__()  经常用于print()方法，有助于我们查看对象的信息
"""


class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def __str__(self):
        '''将对象转化成一个字符串， 一般用于print方 法 '''
        print("重写__str__方法")
        return "名字是： {0},年龄是{1}".format(self.name,self.__age)

'''
    重写__str__方法
    名字是： 林大侠,年龄是19
    重写__str__方法
'''
p = Person("林大侠", 19)
print(p)
s = str(p)