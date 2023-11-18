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
        time.sleep(1)
    return "func1执行完毕"


def func2():
    for k in range(3):
        print(f'上海：第{k}次打印了')
        time.sleep(1)
    return "func2执行完毕"


def main():
    func1()
    func2()


"""
北京：第0次打印啦
北京：第1次打印啦
北京：第2次打印啦
上海：第0次打印了
上海：第1次打印了
上海：第2次打印了
耗时6.023536205291748

"""
if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"耗时{end_time - start_time}")  # 不使用协程，耗时6秒
