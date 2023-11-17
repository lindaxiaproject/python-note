from tkinter import *
from tkinter import messagebox
import random

"""
    place布局管理器可以通过坐标精确控制组件的位置，适用于一些布局更加灵活的场景
"""


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """通过place布局管理器实现扑克牌位置控制"""
        # self.photo = PhotoImage(file="imgs/puke/puke1.gif")
        # self.puke1 = Label(self.master,image=self.photo)
        # self.puke1.place(x=10,y=50)

        self.photos = [PhotoImage(file="files/puke/puke" + str(i + 1) + ".gif") for i in range(10)]
        self.pukes = [Label(self.master, image=self.photos[i]) for i in range(10)]
        for i in range(10):
            self.pukes[i].place(x=10 + i * 40, y=50)

        # 为所有的Label增加事件处理
        self.pukes[0].bind_class("Label", "<Button-1>", self.chupai)


    def chupai(self, event):
        print(event.widget.winfo_geometry())
        print(event.widget.winfo_y())
        if event.widget.winfo_y() == 50:
            event.widget.place(y=30)
        else:
            event.widget.place(y=50)


if __name__ == '__main__':
    root = Tk()
    root.geometry("600x270+200+300")
    app = Application(master=root)
    root.mainloop()
