from tkinter import *
from tkinter import messagebox
import random



root = Tk() ;root.geometry ("200x100")
v = StringVar (root)
v.set("python")
om = OptionMenu (root, v, "java", "python", "vue")

om["width"] = 10
om.pack()


def test1() :
    print("最喜爱的语言 :", v.get())
    #   v.set("尚学堂")      # 直接修改了optionmenu中选中的值


Button (root, text="确定", command=test1).pack()

root.mainloop ()