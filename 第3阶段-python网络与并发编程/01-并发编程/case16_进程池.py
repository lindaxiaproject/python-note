# coding=utf-8
from multiprocessing import Process, current_process
from multiprocessing import Manager

# coding=utf-8
from multiprocessing import Pool
import os
from time import sleep


def func1(name):
    print(f"当前进程的ID:{os.getpid()},{name}")
    sleep(2)
    return name


def func2(args):
    print(args)

"""
    当前进程的ID:19243,sxt1
    当前进程的ID:19242,sxt2
    当前进程的ID:19244,sxt3
    当前进程的ID:19246,sxt4
    当前进程的ID:19245,sxt5
    当前进程的ID:19243,sxt6
    sxt1
    sxt2
    当前进程的ID:19242,sxt7
    sxt3
    当前进程的ID:19244,sxt8
"""
if __name__ == "__main__":
    pool = Pool(5)
    pool.apply_async(func=func1, args=('sxt1',), callback=func2)
    pool.apply_async(func=func1, args=('sxt2',), callback=func2)
    pool.apply_async(func=func1, args=('sxt3',), callback=func2)
    pool.apply_async(func=func1, args=('sxt4',))
    pool.apply_async(func=func1, args=('sxt5',))
    pool.apply_async(func=func1, args=('sxt6',))
    pool.apply_async(func=func1, args=('sxt7',))
    pool.apply_async(func=func1, args=('sxt8',))
    pool.close()
    pool.join()
