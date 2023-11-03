"""
    while循环的语法格式如下：
        while  条件表达式：
            循环体语句
"""

"""【操作】利用while循环打印从0-10的数字"""
num = 0
while num <= 10:
    print(num)
    num += 1

"""利用while循环，计算1-100之间数字的累加和；计算1- 100之间偶数的累加和，计算1-100之间奇数的累加和"""
num = 0
sum_all = 0
while num <= 100:
    sum_all += num
    num +=1
# 1-100所有数的累加和: 5050
print("1-100所有数的累加和:",sum_all)