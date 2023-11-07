"""
    with关键字 （上下文管理器）可以自动管理上下文资源，不论什么原因跳出withk块 ，都能确保文件正确的关闭，并且可以在代码块执行完毕
后自动还原进入该代码块时的现场。

"""

# 使用with管理文件写入操作 【推荐这种方式】
s = ["北京\n", "深圳\n", "北京\n"]
with open(r"/Users/linhong/PycharmProjects/python-note/file/02-test-with.txt", "w") as f:
    f.writelines(s)