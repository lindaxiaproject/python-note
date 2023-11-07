"""
    一般建议尽量捕获可能出现的多个异常（按照先子类后 父类的顺序），并且针对性的写出异常处理代码。为了避免遗漏可
能出现的异常，可以在最后增加BaseException。结构:
    try:
        被监控的、可能引发异常的语句块
    except Exception1:
        处理Exception1的语句块
    except Exception2:
        处理Exception1的语句块
    [....]
    excepte BaseException
        处理可能遗漏的异常的语句块
"""
try:
    a = input("请输入被除数：")
    b = input("请输入除数：")
    c = float(a) / float(b)
    print(c)
except ZeroDivisionError:
    print("异常：除数不能为0")
except TypeError:
    print("异常：除数和被除数都应该为数值类型")
except BaseException as e:
    print(e)
    print(type(e))
