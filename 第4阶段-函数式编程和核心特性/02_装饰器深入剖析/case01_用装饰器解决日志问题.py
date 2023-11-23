# coding=utf-8
# 开闭原则
def mylog(func):
    def inner(*args,**kwargs):
        func(*args,**kwargs)
        print("日志记录....")

    return inner

@mylog # fun1 = mylog(fun1)
def fun1():
    print("使用功能1")

@mylog # fun2 = mylog(fun2)
def fun2(a,b):
    print("使用功能2", a, b)

"""
    使用功能1
    日志记录....
    使用功能2 100 200
    日志记录....
"""
fun1()
fun2(100, 200)
