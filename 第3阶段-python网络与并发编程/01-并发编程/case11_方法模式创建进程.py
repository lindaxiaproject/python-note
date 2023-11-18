# encoding=utf-8
import os
from multiprocessing import Process
from time import sleep


def func1(name):
    print("当前进程ID: ", os.getpid())
    print("当前父进程ID: ", os.getppid())
    print(f"Process:{name} start")
    sleep(3)
    print(f"Process:{name} end")

"""
    打印当前进程ID： 18661
    当前进程ID:  18663
    当前父进程ID:  18661
    Process:p1 start
    当前进程ID:  18664
    当前父进程ID:  18661
    Process:p2 start
    Process:p2 end
    Process:p1 end
"""
if __name__ == '__main__':
    print("打印当前进程ID：", os.getpid())
    # 创建进程
    p1 = Process(target=func1, args=('p1',))
    p2 = Process(target=func1, args=('p2',))
    p1.start()
    p2.start()
