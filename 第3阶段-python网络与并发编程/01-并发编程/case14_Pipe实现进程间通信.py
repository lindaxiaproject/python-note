# encoding=utf-8
import multiprocessing
from time import sleep

def func1(conn1):
    sub_info = "Hello!"
    print(f"进程1--{multiprocessing.current_process().pid}发送数据：{sub_info}")
    sleep(1)
    conn1.send(sub_info)
    print(f"来自进程2:{conn1.recv()}")
    sleep(1)
def func2(conn2):
    sub_info = "你好!"
    print(f"进程2--{multiprocessing.current_process().pid}发送数据：{sub_info}")
    sleep(1)
    conn2.send(sub_info)
    print(f"来自进程1:{conn2.recv()}")
    sleep(1)

"""
    进程1--19034发送数据：Hello!
    进程2--19035发送数据：你好!
    来自进程1:Hello!
    来自进程2:你好!
"""
if __name__ == '__main__':
    #创建管道
    conn1,conn2 = multiprocessing.Pipe()
    # 创建子进程
    process1 =multiprocessing.Process(target=func1,args=(conn1,))
    process2 =multiprocessing.Process(target=func2,args=(conn2,))
    # 启动子进程
    process1.start()
    process2.start()