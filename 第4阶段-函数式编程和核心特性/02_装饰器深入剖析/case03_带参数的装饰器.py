# coding=utf-8
import time


# 带参数的装饰器的典型写法

def mylog(type):
    def decorator(func):
        def infunc(*args, **kwargs):
            if type == "文件":
                print("文件中：日志记录")
            else:
                print("控制台：日志记录")
            return func(*args, **kwargs)

        return infunc

    return decorator


@mylog("文件")
def fun2(a, b):
    print("使用功能2", a, b)

if __name__ == '__main__':
    '''
    文件中：日志记录
    使用功能2 100 200
    '''
    fun2(100, 200)
