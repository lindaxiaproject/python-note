# encoding=utf-8
from threading import Thread
from time import sleep
def func1(name):
    print(f"线程:{name},start...")  # format
    for i in range(3):
        print(f"线程:{name},{i}")
        sleep(1)
    print(f"线程:{name},end!")


if __name__ == '__main__':
    print("开始启动主线程")
    # 创建线程
    t1 = Thread(target=func1, args=("t1",))
    t2 = Thread(target=func1, args=("t2",))
    # 启动线程
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("主线程执行结束")