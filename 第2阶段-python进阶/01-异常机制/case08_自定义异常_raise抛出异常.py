"""
    自定义异常类一般都是运行时异常，通常继承Exception或其子类即可。命名一般以Error、Exception为后缀。
    自定义异常由raise语句主动抛出。
"""

# 自定义异常类和raise语句
class AgeError(Exception): # 继承Exception
    def __init__(self, errorInfo):
        Exception.__init__(self)
        self.errorInfo = errorInfo
    def __str__(self):
        return str(self.errorInfo)+ ",年龄错误！应该在1-150之间"

# #如果为True，则模 块是作为独立文件运行，可以执行测试代码
if __name__ == "__main__":
    age = int(input("请出入一个年龄："))
    if age < 1 or age > 150:
        raise  AgeError(age)
    else:
        print("正常的年龄：", age)


