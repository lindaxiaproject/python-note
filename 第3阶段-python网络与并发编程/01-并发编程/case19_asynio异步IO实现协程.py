# coding=utf-8
from multiprocessing import Process, current_process
from multiprocessing import Manager

import time
import asyncio


async def func1():
    for i in range(3):
        print(f'北京：第{i}次打印啦')
        await asyncio.sleep(1)
    return "func1执行完毕"


async def func2():
    for k in range(3):
        print(f'上海：第{k}次打印了')
        await asyncio.sleep(1)
    return "func2执行完毕"


async def main():
    res = await asyncio.gather(func1(), func2())
    # await异步执行func1方法
    # 返回值为函数的返回值列表,本例为["func1执行完毕", "func2执行完毕"]'
    print(res)

"""

北京：第0次打印啦
上海：第0次打印了
北京：第1次打印啦
上海：第1次打印了
北京：第2次打印啦
上海：第2次打印了
['func1执行完毕', 'func2执行完毕']
耗时3.004145860671997
"""
if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"耗时{end_time - start_time}")  # 不使用协程，耗时6秒
