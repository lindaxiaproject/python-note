

class AAA():
    def __init__(self,func):
        print("我是AAA.init()")
        print(func.__name__)
        self.__func = func
    def __call__(self, *args, **kwargs):
        print("--装饰器中的功能---")
        self.addFunc()
        self.__func()

    def addFunc(self):
        print("权限认证")
        print("日志打印")

@AAA
def test1():
    print("我是功能1")

"""
    我是AAA.init()
    test1
    --装饰器中的功能---
    权限认证
    日志打印
    我是功能1
"""
# 本身test1指向函数test1，但是装饰器将test1指向了对象。
# 对象本身不可以被调用，但是重写__call__方法之后则会被调用

test1()