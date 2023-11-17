from tkinter import *
from tkinter import messagebox


# 通过类 Tk 的无参构造函数
root = Tk()
root.title("这是我的第1个GUI程序！")
# #宽度500，高度300；距屏幕左边100，距屏幕上边200
root.geometry("500x300+100+200")


# 在主窗口中，添加各种可视化组件，比如：按钮（Button）、文本框（Label）等。
btn01 = Button(root)
btn01["text"] = "点我就送花"

# 通过几何布局管理器，管理组件的大小和位置
btn01.pack()

# 通过绑定事件处理程序，响应用户操作所触发的事件（比如：单击、双击等）
def songhua(e):
    messagebox.showinfo("Message", "林大侠送你一朵玫瑰花")
    print("爱你哟")


btn01.bind("<Button-1>", songhua)

# 调用组件的mainloop()方法，进入时间循环
root.mainloop()
