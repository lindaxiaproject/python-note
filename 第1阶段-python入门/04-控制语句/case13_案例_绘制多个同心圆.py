import turtle

""" 使用海龟绘图，绘制同心圆 """
p = turtle.Pen()  #画笔对象
radius = [x*10 for x in range(1,11)]

#10,20,30,40...
my_colors = ("red","green","yellow","black")
p.width(4)

for r,i in zip(radius,range(len(radius))):
    p.penup()
    p.goto(0,-r)
    p.pendown()
    p.color(my_colors[i%len(my_colors)])
    p.circle(r)

turtle.done()  #程序执行完毕，窗口在