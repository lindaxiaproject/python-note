from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label01 = Label(self, text="用户名")
        self.label01.pack()

        v1 =  StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack()
        v1.set("admin")
        print(v1.get());print(self.entry01.get())

        # 创建密码框
        self.label02 = Label(self, text="密码")
        self.label02.pack()

        v2 = StringVar()
        # 输入的密码用星号代替
        self.entry02 = Entry(self, textvariable=v2, show="*")
        self.entry02.pack()
        Button(self, text="登陆", command=self.login).pack()


    def login(self):
        username = self.entry01.get()
        pwd = self.entry02.get()

        print("去数据库比对用户名和密码～")
        print("用户名："+ username)
        print("密码：" + pwd)

        if username == "lindaxia" and pwd =="1234":
            messagebox.showinfo("林大侠学习系统","登陆成功，欢迎开始学习！")
        else:
            messagebox.showinfo("林大侠学习系统","登陆失败，用户名或密码错误！")

if __name__ == '__main__':
    root = Tk()
    root.geometry("400x130+200+300")
    app = Application(master=root)
    root.mainloop()
