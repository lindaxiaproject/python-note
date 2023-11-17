from tkinter import *
from tkinter import messagebox
import random

"""
    Scale(移动滑块)用于在指定的数值区间，通过滑块的移动来选择值。
"""

root = Tk();
root.geometry("400x150")


def test1(value):
    print("滑块的值 :", value)
    newFont = ("宋体", value)
    a.config(font=newFont)

s1 =Scale(root,from_=10,to=50,length=200,tickinterval=5,orient=HORIZONTAL,command=test1)
s1.pack()

a = Label(root,text="林大侠学python",width=10,height=1,bg="black",fg="white")
a.pack()
root.mainloop()
