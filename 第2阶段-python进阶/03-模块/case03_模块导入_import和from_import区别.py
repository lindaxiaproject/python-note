import math as m
import math
from math import sqrt, sin
import Calculator

"""
    import 语句的基本语法格式如下：
         import  模块名                  #导入一个模块
         import  模块1，模块2…            #导入多个模块
         import  模块名   as 模块别名      #导入模块并使用新名字

    import加载的模块分为四种类型：
        使用python编写的代码
        已被编译为共享库或DLL的C或C++扩展
        一组模块的包
        使用C编写并链接到python解释器的内置模块

    一般通过 import 语句实现模块的导入和使用，本质上就是用了内置函数__import__()

    当我们通过import导入一个模块时, python解释器进行执行，最终 会生成一个对象，这个对象就代表了被加载的模块.
"""


# 4310500672
print(id(m))
# 4310500672
print(id(math))
# <class 'module'>
print(type(math))
# 3.141592653589793
print(math.pi)
# 2.0
print(m.sqrt(4)) # 开方运算

"""
    Python中可以使用 from … import 导入模块中的成员(导入的是模块中的函数/类)
    from  模块名  import  成员1 ，成员2 ，…
"""
# 9.0
print(sqrt(81))
print(Calculator.Add(30, 40))