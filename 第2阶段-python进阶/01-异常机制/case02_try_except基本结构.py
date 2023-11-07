"""
    try...一个except结构：
            try:
                被监控的可能引发异常的语句块
            except  BaseException [as  e]:
                异常处理语句块

"""



#  测试简单的0不能做除数异常，遇到异常的执行顺序
'''
step1
step3
division by zero
step4
'''
try:
    print("step1")
    a = 3 /0
    print("step2")
except BaseException as e:
    print("step3")
    print(e)

print("step4")