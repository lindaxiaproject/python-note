from tkinter import *
from tkinter import messagebox
import random


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """通过grid布局实现计算器的界面"""
        btnText = (("MC", "M+", "M-", "MR"),
                   ("C", " ±", "/", "    "),
                   (7, 8, 9, "-"),
                   (4, 5, 6, "+"),
                   (1, 2, 3, "="),
                   (0, "."))

        Entry(self).grid(row=0, column=0, columnspan=4, pady=10)

        for rindex, r in enumerate(btnText):
            for cindex, c in enumerate(r):
                if c == "=":
                    Button(self, text=c, width=2) \
                        .grid(row=rindex + 1, column=cindex, rowspan=2, sticky=NSEW)
                elif c == 0:
                    Button(self, text=c, width=2) \
                        .grid(row=rindex + 1, column=cindex, columnspan=2, sticky=NSEW)

                elif c == ".":
                    Button(self, text=c, width=2) \
                        .grid(row=rindex + 1, column=cindex + 1, sticky=NSEW)
                else:
                    Button(self, text=c, width=2) \
                        .grid(row=rindex + 1, column=cindex, sticky=NSEW)

"""
    通过 grid 布局-实现计算器软件界面。
    根据实际简易计算器的按键分布，设计一个相仿的计算器界面，相应的功能暂不需要实现。
"""
if __name__ == '__main__':
    root = Tk()
    root.geometry("200x200+200+300")
    app = Application(master=root)
    root.mainloop()
