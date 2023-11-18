#encoding=utf-8

from threading import Thread, Lock
from time import  sleep

# 账号类
class Account:
    def __init__(self, money, name):
            self.money = money
            self.name = name
# 模拟提款操作
class Drawing(Thread):
    # 定义构造函数
    def __init__(self, drawingNum, account):
        Thread.__init__(self)
        self.drawingNum = drawingNum # 取款数
        self.account = account # 账号
        self.expenseTotal = 0 # 一共取了多少

    def run(self):
        lock1.acquire()
        # 账号里面的钱 小于 本次取款的钱
        if self.account.money-self.drawingNum < 0:
            print("账户余额不足！")
            return
        sleep(1) # 判断完可以取钱，则阻塞，为了测试发生冲突问题
        self.account.money -= self.drawingNum
        self.expenseTotal += self.drawingNum
        lock1.release()
        print(f"账户:{self.account.name},余额是:{self.account.money} \n")
        print(f"账户:{self.account.name},总共取了:{self.expenseTotal} \n")


'''
    账户:lindaxia,余额是:20
    账户:lindaxia,总共取了:80
    账户:lindaxia,余额是:-60
    账户:lindaxia,总共取了:80

'''
if __name__ == '__main__':
    a1 = Account(100, "lindaxia")
    lock1 = Lock()
    draw1 = Drawing(80, a1) # 定义取钱线程对象a1；
    draw2 = Drawing(80, a1) # 定义取钱线程对象a2；
    draw1.start() # a1取钱
    draw2.start() # a2取钱

