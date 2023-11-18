# encoding=utf-8
from multiprocessing import Process, Queue


class MyProcess(Process):
    def __init__(self, name, mq):
        Process.__init__(self)
        self.name = name
        self.mq = mq

    def run(self):
        print("Process:{} start".format(self.name))
        print('--------------', self.mq.get(), '-------------')
        self.mq.put(self.name)
        print("Process:{}end".format(self.name))

"""
    Process:p0 start
    -------------- 1 -------------
    Process:p0end
    Process:p2 start
    -------------- 2 -------------
    Process:p2end
    Process:p1 start
    -------------- 3 -------------
    Process:p1end
    p0
    p2
    p1
"""
if __name__ == '__main__':
    # 创建进程列表
    t_list = []
    mq = Queue()
    mq.put('1')
    mq.put('2')
    mq.put('3')
    # 循环创建进程
    for i in range(3):
        t = MyProcess('p{}'.format(i), mq)
        t.start()
        t_list.append(t)
    # 等待进程结束
    for t in t_list:
        t.join()
    print(mq.get())
    print(mq.get())
    print(mq.get())
