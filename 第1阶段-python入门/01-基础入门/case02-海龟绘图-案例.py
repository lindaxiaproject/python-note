import turtle # 导入海龟绘图模块

# 显示箭头
turtle.showturtle()
# 写字符串
turtle.write("kkk, 你好 ，我是林大侠")
# 前进300个像素
turtle.forward(300)
# 画笔改变颜色：red
turtle.color("red")
turtle.left(90)
# 前进300个像素
turtle.forward(300)
turtle.goto(0,50)
turtle.goto(0,0)
turtle.goto(0,300)
# 抬起笔，这样移动时，路径就不会画出来
turtle.penup()
turtle.goto(0,300)
turtle.pendown()
# 画圆
turtle.circle(100)
# 程序结束，保持窗口存在
turtle.done()