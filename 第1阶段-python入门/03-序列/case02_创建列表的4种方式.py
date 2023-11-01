a = list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

"""
    range()可以帮助我们非常方便的创建整数列表
        start参数：可选，表示起始数字。默认是0
        end参数：必选，表示结尾数字
        step参数：可选，表示步长，默认为1
        
    python3中range()返回的是一个range对象，而不是列表.
    我们需要通过list()方法将其转换成列表对象
    
"""
# [3, 5, 7, 9, 11, 13]
b = list(range(3, 15, 2))
print(b)

"""
    推倒式生成列表
"""
# 循环创建多个元素
c = [x * 2 for x in range(5)]
# [0, 2, 4, 6, 8]
print(c)


