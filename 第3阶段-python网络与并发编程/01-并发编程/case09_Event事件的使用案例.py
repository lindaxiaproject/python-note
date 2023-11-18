# encoding=utf-8
import threading
import time
from threading import Thread, Lock
from time import sleep

"""
    小伙伴门围着吃火锅，当菜上齐了，请客的主人说：开吃！
    于是小伙伴一起动筷子，这种场景是如何实现的？
"""
def chihuoguo(name):
    # 等待事件，进入等待阻塞状态
    print(f'{name}已经启动')
    print(f'小伙伴{name}已经进入到就餐状态！')
    time.sleep(1)
    '''
    调用该方法的线程会被阻塞，如果设置了timeout参数，超时后，
    线程会停止阻塞继续执行；
    '''
    event.wait()
    # 收到事件后进入到运行状态
    print(f'{name}收到通知了')
    print(f'小伙伴{name}开始吃！')

"""

    lindaxia已经启动
    小伙伴lindaxia已经进入到就餐状态！
    kkk已经启动
    小伙伴kkk已经进入到就餐状态！
    ------>主线程通知小伙伴开吃！
    lindaxia收到通知了
    小伙伴lindaxia开始吃！
    kkk收到通知了
    小伙伴kkk开始吃！
"""
if __name__ == '__main__':
    event = threading.Event()
    # 创建线程
    t1 = threading.Thread(target=chihuoguo, args=("lindaxia",))
    t2 = threading.Thread(target=chihuoguo, args=("kkk",))
    # 开启线程
    t1.start()
    t2.start()
    time.sleep(10)
    # 发送事件通知
    print('------>主线程通知小伙伴开吃！')
    ''' 将event的标志设置为True，调用wait方法的所有线程将被唤醒 '''
    event.set()
