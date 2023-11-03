"""
    if语句单分支结构的语法形式
        if  条件表达式:
             语句/语句块

    【操作】输入一个数字，小于10，则打印这个数字
"""
num = 8
# num = input("输入一个数字: ")
if int(num) < 10:
    # 小于10的整数:8
    print("小于10的整数:" + str(num))

if 3:
    # ok!
    print("ok!")
a = []
if a:
    print("空列表, False")
b = ""
if b:
    print("空字符串, False")
if "False":
    # 非空字符串, True
    print("非空字符串, True")