"""
    由于文件底层是由操作系统控制，所以我们打开的文件对象必须显式调用close() 方法关闭文件对象。
    当调用close() 方法时，首先会把缓冲 区数据写入文件(也可以直接调用flush() 方法)，再关闭文件，释放文件对象。

    为了确保打开的文件对象正常关闭， 一般结合异常机制的 finally 或者with 关键字实现无论何种情况都能关闭打开的文件对象!

"""

# 结合异常机制的finally,确保关闭文件对象
try:
    f = open(r"/Users/linhong/PycharmProjects/python-note/file/02-test-finally.txt", "a")
    s = "林大侠"
    f.write(s)
except BaseException as e:
    print(e)
finally:
    f.close()