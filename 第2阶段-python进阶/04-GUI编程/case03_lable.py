""" 测试Lable组件的基本用法，使用面向对象的方式 """
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """ 一个经典的GUI程序的类的写法 """
    def __init__(self, master=None):
        # super()代表的是父类的定义，而不是父类对象
        super().__init__(master)
        self.master = master
        self.pack()  # 通过几何布局管理器，管理组件的大小和位置
        self.createWidget()

    def createWidget(self):
        """ 创建组件 """
        self.lable01 = Label(self, text="全干程序员", width=10, height=2, bg="black", fg="white")
        self.lable01["text"] = "666"
        self.lable01.config(fg="red", bg="green")
        self.lable01.pack()
        self.lable02 = Label(self, text="林大侠学python", width=10, height=2, bg="blue", fg="white", font=("黑体", 30))
        self.lable02.pack()

        # 显示图像 把photo声明成全局变量。如果是全局变量，本方法执行完毕后，图像对象销毁，窗口显示不出来
        global photo
        photo = PhotoImage(file="files/logo.gif")
        self.label03 = Label(self, image=photo)
        self.label03.pack()
        self.label04 = Label(self, text="北京西城\n 全栈工程师\n 林大侠，很帅！",
                             borderwidth=5, relief="groove", justify="right")
        self.label04.pack()



'''
Label（标签）有这样一些常见属性：
    1. width,height：
        用于指定区域大小，如果显示是文本，则以单个英文字符大小为单位(一个汉字宽度占 2 个字符位置，高度和英文字符一样)；
        如果显示是图像，则以像素为单位。默认值是 根据具体显示的内容动态调整。
    2. font
        指定字体和字体大小，如：font  = (font_name,size)
    3. image :
        显示在 Label 上的图像， 目前 tkinter 只支持 gif 格式。
    4. fg 和 bg
        fg（foreground） :前景色、bg（background） :背景色
    5. justify
        针对多行文字的对齐，可设置 justify 属性，可选值"left", "center" or "right" 【示例】Label（标签）的用法
'''
if __name__ == '__main__' :
    root = Tk()
    root.geometry("400x100+200+300")
    app = Application(master=root)
    root.mainloop()
