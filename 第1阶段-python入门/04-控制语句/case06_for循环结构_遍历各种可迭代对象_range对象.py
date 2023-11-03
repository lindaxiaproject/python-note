"""
    for  变量    in  可迭代对象：
        循环体语句

Python包含以下几种可迭代对象：
    1       序列。包含：字符串、列表、元组、字典、集合
    2       迭代器对象（iterator）
    3       生成器函数（generator）
    4       文件对象
"""

"""遍历一个元组或列表"""
for x in (20, 30, 40):
    print(x)

"""遍历字符串中的字符"""
for x in "lindaxia":
    print(x)

"""遍历字典"""
d = {'name': 'lindaxia', 'age': 18, 'address': '北京西城'}
for x in d:
    # 遍历字典所有的key
    print(x)

for x in d.keys():
    # 遍历字典所有的key
    print(x)

for x in d.values():
    # 遍历字典所有的value
    print(x)

"""
    range对象 是一个迭代器对象，用来产生指定范围的数字序列。格式为: range(start, end  [,step])
    生成的数值序列从start开始到end结束(不包含end）。若没有填写start，则默认从0开.step是可选的步长，默认为1。
"""
for i in range(10):
    # 产生序列：  0 1 2 3 4 5 6 7 8 9
    print(i)
for i in range(3, 10):
    # 产生序列： 3 4 5 6 7 8 9
    print(i)
for i in range(3, 10, 2):
    # 产生序列：  3 5 7 9
    print(i)

"""
    利用for循环，
        计算1-100之间数字的累加和
        计算1-100 之间偶数的累加和
        计算1-100之间奇数的累加和
"""
# 1-100所有数的累加和
sum_all = 0
# 1-100偶数的累加和
sum_even = 0
# 1-100奇数的累加和
sum_odd = 0

for num in range(101):
    sum_all += num
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
# 1-100累加总和5050,奇数和2500,偶数和2550
print("1-100累加总和{0},奇数和{1},偶数和{2}".format(sum_all, sum_odd, sum_even))