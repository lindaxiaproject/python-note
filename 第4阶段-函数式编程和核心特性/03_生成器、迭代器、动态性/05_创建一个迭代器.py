"""
    创建1个依次返回10，20，30...这样数字的迭代器
"""
class MyNumbers:
    # 返回一个特殊的迭代器对象
    def __iter__(self):
        self.num = 10
        return  self
    # 返回下一个迭代器对象
    def __next__(self):
        if self.num < 40:
            x = self.num
            self.num += 10
            return  x
        else:
            raise stopIteration

myClass = MyNumbers()
myiter = iter(myClass)

"""
    10
    20
    30
"""
print(next(myiter))
print(next(myiter))
print(next(myiter))

