# 注释函数定义的方式
def stringify(num: int) -> str:
    return str(num)


print
stringify(10)


# 指定多个参数的方式
def plus(num1: int, num2: int) -> int:
    return num1 + num2


print
plus(10, 20)


# 在类型注释后为参数添加默认值
def func1(num1: int, my_float: float = 3.5) -> float:
    return num1 + my_float


print
func1(10, 20.5)