# coding=utf-8
from multiprocessing import Process, current_process
from multiprocessing import Manager

# coding=utf-8
from multiprocessing import Pool
import os
from time import sleep

import time


def func1():
    for i in range(3):
        print(f'北京：第{i}次打印啦')
        yield  # 只要方法包含了yield，就变成一个生成器
        time.sleep(1)
    return "func1执行完毕"


def func2():
    g = func1()  # func1是一个生成器，func1()就不会直接调用，需要通过next()或for循环调用
    print(type(g))
    for k in range(3):
        print(f'上海：第{k}次打印了')
        next(g)  # 继续执行func1的代码
        time.sleep(1)
    return "func2执行完毕"

"""
上海：第0次打印了
北京：第0次打印啦
上海：第1次打印了
北京：第1次打印啦
上海：第2次打印了
北京：第2次打印啦
耗时5.01768684387207
"""
if __name__ == '__main__':
    # 有了yield，我们实现了两个任务的切换+保存状态
    start_time = time.time()
    func2()
    end_time = time.time()
    print(f"耗时{end_time - start_time}")  # 耗时5.0 秒，效率差别不大
