"""
    形参与实参：
        1.圆括号内是形式参数列表，有多个参数则使用逗号隔开
        2.定义时形式参数不需要声明类型，也不需要制定函数返回值类型
        3.调用时的实际参数必须与形参列表一一对应

"""

# 定义一个函数，实现两个数的比较，并返回较大的值
def printMax(a, b):
    '''实现两个数的比较，并返回较大的值'''
    if a > b:
        print(a, '为较大值')
        return a
    else:
        print(b, '为较大值')
        return b

# 20 为较大值
printMax(10, 20)
# 50 为较大值
printMax(50, 20)


"""
    文档字符串(函数的注释)
        通过三个单引号或者三个双引号来实现
        
"""

# 测试文档字符串的使用

def print_star(n):
    '''
    根据传入的n,打印多个星号
    :param n: 传入的数字
    :return: n个星号拼接的字符串
    '''
    s = "*"*n
    print(s)
    return s
#调用 help(函数名) 可打印输出函数的文档字符串
help(print_star)
print(print_star.__doc__)
print_star(3)