"""

    finally 块由于是否发生异常都会执行，通常我们放释放资源的代码。
         其实，我们可以通过with上下文管理，更方便的实现释放资源的操作。

         with  context_expr [ as  var]：
            语句块


"""
# 上下文管理文件操作
with open("/Users/linhong/Desktop/test.txt", "r") as f:
    for line in f:
        print(line)
    # content = f.readline()
    print(line)
print("继续执行其它代码")
print("程序结束")