# encoding=utf-8

from threading import Thread
from time import sleep
from queue import Queue

def producer():
     num = 1
     while True:
         if queue.qsize() < 5:
             print(f"生产{num}号，大馒头")
             queue.put(f'大馒头：{num}号')
             num +=1
         else:
            print('馒头框满了，等待来人消费啊！')
            sleep(1)
def consumer():
    while True:
        print(f'获取馒头:{queue.get()}')
        sleep(1)

"""
    生产1号，大馒头
    生产2号，大馒头
    生产3号，大馒头
    生产4号，大馒头
    生产5号，大馒头
    馒头框满了，等待来人消费啊！
    获取馒头:大馒头：1号
    获取馒头:大馒头：2号
    生产6号，大馒头
    生产7号，大馒头
    ....
"""
if __name__ == '__main__':
    queue = Queue()
    p = Thread(target=producer)
    p.start()
    c = Thread(target=consumer)
    c.start()
    c2 = Thread(target=consumer)
    c2.start()
