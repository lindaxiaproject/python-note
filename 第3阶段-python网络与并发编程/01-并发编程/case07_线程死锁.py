# encoding=utf-8

from threading import Thread, Lock
from time import sleep


def fun1():
    lock1.acquire()
    print('fun1拿到菜刀')
    sleep(2)
    lock2.acquire()
    print('fun1拿到锅')
    lock2.release()
    print('fun1释放锅')
    lock1.release()
    print('fun1释放菜刀')

def fun2():
    lock2.acquire()
    print('fun2拿到锅')
    lock1.acquire()
    print('fun2拿到菜刀')
    lock1.release()
    print('fun2释放菜刀')
    lock2.release()
    print('fun2释放锅')


if __name__ == '__main__':
    lock1 = Lock()
    lock2 = Lock()
    t1 = Thread(target=fun1)
    t2 = Thread(target=fun2)
    t1.start()
    t2.start()
