from tkinter import *
from tkinter import messagebox
import random

from tkinter import *
from tkinter.colorchooser import *

from tkinter import *
from tkinter.filedialog import *

root = Tk();root.geometry("400x100")


def test1():
    with askopenfile(title="上传文件", initialdir="d :", filetypes=[("文本文件", ".txt")]) as f: show["text"] = f.read()
Button (root,text="选择读取的文本文件",command=test1).pack()

show = Label(root,width=40,height=3,bg="green")
show.pack()

root.mainloop ()