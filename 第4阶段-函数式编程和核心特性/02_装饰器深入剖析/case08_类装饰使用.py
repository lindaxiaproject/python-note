# coding = utf-8

class MyLogDecorator():
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("日志记录.....")
        return  self.func(*args, **kwargs)

@MyLogDecorator
def fun2():
    print("使用功能2")

if __name__ == '__main__':
    """
    日志记录.....
    使用功能2
    """
    fun2()