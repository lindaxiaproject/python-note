"""
    嵌套函数：在函数内部定义的函数！
"""

def  outer():
    print('outer running...')
    def inner():
        print('inner running...')
    inner()


outer()

def printName(isChinese,name,familyName):
    # 内部函数
    def inner_print(a,b):
        print("{0} {1}".format(a,b))

    if isChinese:
        inner_print(familyName,name)
    else:
        inner_print(name,familyName)

printName(True,"林大侠","林")
printName(False,"lindaxia","kk")