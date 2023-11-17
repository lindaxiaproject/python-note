from tkinter import *
from tkinter import messagebox
import random

"""
    lambda 表达式定义的是一个匿名函数，只适合简单输入参数，简单计算返回结果，不适合 功能复杂情况。
    lambda 定义的匿名函数也有输入、也有输出，只是没有名字。语法格式如下： lambda 参数值列表：表达式
        场景：在事件里面帮助我们穿参
"""

root = Tk();
root.geometry("270x50")


def mouseTest1():
    print("command 方式，简单情况：不涉及获取 event 对象，可以使用")


def mouseTest2(a, b):
    print("a= {0},b= {1}".format(a, b))


Button(root, text="测试 command1",
       command=mouseTest1).pack(side="left")

Button(root, text="测试 command2",
       command=lambda: mouseTest2("林大侠", "haha")).pack(side="left")

root.mainloop()
