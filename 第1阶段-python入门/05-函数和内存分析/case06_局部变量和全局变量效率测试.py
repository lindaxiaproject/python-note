import time

"""
    局部变量的查询和访问速度比全局变量快，优先考虑使用，尤其是在循环的时候。
"""

a = 1000
def test01():
    start = time.time()
    global a
    for i in range(100000000):
        a += 1
    end = time.time()

    print("耗时{0}".format((end - start)))


def test02():
    start = time.time()
    c = 1000
    for i in range(100000000):
        c += 1
    end = time.time()
    print("耗时{0}".format((end - start)))
# 耗时3.67496395111084
test01()
# 耗时2.088636875152588 局部变量效率更快
test02()
