"""
    除了继承，“组合”也能实现代码的复用！“组合”核心是“将父类对象作为子类的属性”。

    组合的核心是“将父类对象作为子类的属性”
    is-a 关系，我们可以使用“继承”
     has-a 关系，我们可以使用“组合”
"""

class CPU:
    def calculate(self):
        print("正在计算，算个123333")


class Screen:
    def show(self):
        print("我是显示屏")

class MobilePhone():
    def __init__(self, cpu ,screen):
        self.cpu = cpu
        self.screen = screen


c = CPU()
s = Screen()
m = MobilePhone(c, s)
m.cpu.calculate()
m.screen.show()



