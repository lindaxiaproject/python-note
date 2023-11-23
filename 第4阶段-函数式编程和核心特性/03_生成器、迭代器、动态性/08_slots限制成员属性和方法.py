class Person():
    __slots__ = {"name","age"}
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print("人是铁饭是钢，要吃！")


if __name__ == '__main__':
    p1 = Person("lindaxia",18)
    # AttributeError: 'Person' object has no attribute 'gender'
    p1.gender = "man"