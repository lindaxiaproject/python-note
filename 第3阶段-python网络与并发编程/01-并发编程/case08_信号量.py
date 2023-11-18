# encoding=utf-8

from threading import Thread, Lock
from time import sleep
from multiprocessing import Semaphore

"""
    一个房间1次只允许两个人通过，若不使用信号量，会造成所有人都进入到这个房子
    若只允许1人通过可以用锁-Lock()
"""
def home(name, se):
    se.acquire()
    print(f"{name}进入房间")
    sleep(3)
    print(f"****{name}走出房间")
    se.release()



"""


"""
if __name__ == '__main__':
    se = Semaphore(5) # 创建信号量对象
    for i in range(7):
        t = Thread(target=home, args=(f"tom{i}", se))
        t.start()
