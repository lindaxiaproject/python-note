"""
    如果一个函数中包含了yield关键字，那么这个函数就不再是一个普通函数，调用函数就是创建了一个
    生成器对象。
    生成器函数：其实就是利用关键字yield一次性返回一个结果，阻塞，重新开始
"""
def test():
    print("start")
    i = 0
    while i < 3:
        yield i # 程序会挂起，返回
        print(f"i:{i}")
        i +=1
    print("end")
    return "done"

if __name__ == '__main__':
    a = test()
    # <generator object test at 0x102755d90>
    print(a)
    '''
    start
    i:0
    i:1
    '''
    a.__next__()
    a.__next__()
    a.__next__()
