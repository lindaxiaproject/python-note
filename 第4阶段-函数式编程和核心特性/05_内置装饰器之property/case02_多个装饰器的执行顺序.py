# coding=utf-8
import time

def mylog(func):
    print("mylog, start")

    def infunc():
        print("日志记录 start....")
        func()
        print("日志记录 end!")

    print("mylog, end")
    return infunc


def cost_time(func):
    print("cost time start")
    def infunc():
        print("开始记时...")
        start = time.time()
        func()
        end = time.time()
        print(f"花费时间:{end - start}")
        return end - start

    print("cost time end")
    return infunc
@mylog
@cost_time
def fun2():
    print("fun2, start")
    time.sleep(3)
    print("fun2, end")

"""
    cost time start
    cost time end
    mylog, start
    mylog, end
    日志记录 start....
    开始记时...
    fun2, start
    fun2, end
    花费时间:3.0021517276763916
    日志记录 end!
"""
fun2()
