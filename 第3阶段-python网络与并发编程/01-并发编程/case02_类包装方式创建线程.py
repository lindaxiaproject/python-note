# encoding=utf-8
from threading import Thread
from time import sleep

"""
    自定义线程类
"""


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        print(f"线程{self.name},start...")
        for i in range(3):
            print(f"线程{self.name},{i}")
            sleep(3)
        print(f"线程{self.name},end!")


if __name__ == '__main__':
    print("主线程, start....")
    # 创建线程(类的方式)
    t1 = MyThread('t1')
    t2 = MyThread('t2')
    # 启动线程
    t1.start()
    t2.start()
    print("主线程，end!")
