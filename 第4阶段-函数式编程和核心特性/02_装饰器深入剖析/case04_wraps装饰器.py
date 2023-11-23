# coding=utf-8
from functools import wraps
# 带参数的装饰器的典型写法

def mylog(func):
    @wraps(func)
    def infunc(*args, **kwargs):
        """包装的内部函数"""
        print("日志记录.....")
        print("函数文档：", func.__doc__)
        return func(*args, **kwargs)
    return infunc


@mylog
def fun2():
    """强大的功能2"""
    print("使用功能2")


if __name__ == '__main__':
    '''
    文件中：日志记录
    使用功能2 100 200
    '''
    fun2()
    print("函数文档--->", fun2.__doc__)
