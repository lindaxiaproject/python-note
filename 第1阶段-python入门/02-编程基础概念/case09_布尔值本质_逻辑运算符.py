a = True
b = 3
c = a + b
""" 
    python3 布尔值有True 、 False 对应的就是 1、0
    输出结果为4 True本质就是整数"1" 
"""
print(c)

#  空字符串的布尔类型的值： False
print('空字符串的布尔类型的值：', bool(""))
# 空列表的布尔类型的值： False
print('空列表的布尔类型的值：', bool([]))
# None布尔类型的值： False
print('None布尔类型的值：', bool(None))
# 0布尔类型的值： False
print('0布尔类型的值：', bool(0))
# 字符串True和False转成布尔类型都是True： True
print('字符串True和False转成布尔类型都是True：', bool("False"))

"""
    逻辑运算符
"""
aa = True
bb = False
# （逻辑与）输出：False
print(aa and bb)
# （逻辑或）输出：True
print(aa or bb)


"""
    比较运算符
    ==、 != 、>、 <、......
"""
d = 10 > 30 and 50 < 100
# ZeroDivisionError: division by zero
# e = 100 < 200 and 50 < (30 / 0)
# 会发生"短路" , 不会执行"50 < (30 / 0)" 比较运算
e = 100 > 200 and 50 < (30 / 0)
print(e)

f = 300
g = 100 < f < 500
h = 100 < f and f < 500
# 输出: True True
print(g , h)


a = 0b1101
b = 0b1001
c = a|b
print(bin(c))

"""
 字符串拼接
"""
aaa = "3"
bbb = 4
# 输出 34
print(aaa + str(bbb))
# 输出 值类型为字符串类型 <class 'str'>
print(type(aaa + str(bbb)))

