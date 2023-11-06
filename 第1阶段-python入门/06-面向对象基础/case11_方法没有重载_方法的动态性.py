"""
    如果我们在类体中定义了多个重名的方法，只有最后一个方法有效。
        建议：不要使用重名的方法！  Python中方法没有重载。

"""

class Person:
    def say_hi(self):
        print("hello")
    def say_hi(self, name):
        print("{0},hello".format(name))

p1 = Person()
# 林大侠,hello
p1.say_hi("林大侠")


"""
    Python是动态语言，我们可以动态的为类添加新的方法，或者动态 的修改类的已有的方法
"""
# 测试方法的动态性
class Person:
    def work(self):
        print("努力上班！")

def play_game(s):
    print("玩游戏")
def work2(s):
    print("好好工作，努力上班！")

# 修改类中方法（动态性）
Person.play = play_game
Person.work = work2

'''
    玩游戏
    好好工作，努力上班！
'''
p = Person()
p.play()
p.work()
