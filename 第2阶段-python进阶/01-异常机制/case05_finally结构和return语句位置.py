"""
    try...except...finally结构
        在 try...except...finally结构中finally块无论是否发生异常都会被执行；通常用来释放 try 块中申请的资源。
"""


# try:
#     a = input("请输入被除数：")
#     b = input("请输入除数：")
#     c = float(a) / float(b)
#     print(c)
# except BaseException as e:
#     print(e)
# else:
#     print("除的结果是：", c)
# finally:
#     print("我是finally中的语句，无论发生异常与否，都执行！")
# print("程序结束！")

# 读取桌面文件，保证关闭文件资源
try:
    f = open("/Users/linhong/Desktop/test.txt", "r")
    content = f.readline()
    print(content)
except BaseException as e:
    print(e)
finally:
    print("关闭文件资源")
    f.close()

print("继续执行其它代码")
print("程序结束")