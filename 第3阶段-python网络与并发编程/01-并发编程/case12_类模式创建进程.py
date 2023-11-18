# encoding=utf-8
import os
from multiprocessing import Process
from time import sleep


class Myprocess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print(f"Process:{self.name} start")
        sleep(3)
        print(f"Process:{self.name} end")

"""
    打印当前进程ID： 18760
    Process:p1 start
    Process:p2 start
    Process:p1 end
    Process:p2 end
"""
if __name__ == '__main__':
    print("打印当前进程ID：", os.getpid())
    # 创建进程
    p1 = Myprocess("p1")
    p2 = Myprocess("p2")
    p1.start()
    p2.start()
