#coding=utf-8


"""
    本次内容：是装饰器的基础
"""


def outfunc(func):
    # 定义闭包
    def infunc(*args, **kwargs):
        print("日志记录 start...")
        func(*args, **kwargs)
        print("日志记录 end...")
    return infunc


def fun1():
    # print("日志记录.....")
    print("使用功能1")


def fun2():
    # print("日志记录.....")
    print("使用功能2")


def fun3(a, b, c):
    # print("日志记录.....")
    print(f"使用功能3 {a},{b},{c}")

'''
    4381247664
    4381261056
    日志记录 start...
    使用功能1
    日志记录 end...
    日志记录 start...
    使用功能2
    日志记录 end...
    日志记录 start...
    使用功能3 100,200,300
    日志记录 end...
'''
print(id(fun1))
fun1 = outfunc(fun1)
print(id(fun1))
fun1()

fun2 = outfunc(fun2)
fun2()

fun3 = outfunc(fun3)
fun3(100, 200, 300)

