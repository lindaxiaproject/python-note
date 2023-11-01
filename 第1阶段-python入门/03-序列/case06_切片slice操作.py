"""
    切片是Python序列及其重要的操作，适用于列表、元组、字符串等
    	[:] 提取整个列表
    	[start:] 从start索引开始到结尾
        [:end]从头开始到end-1
        [start:end] 从start到end-1
        [start:end:step] 从start提取到end-1 ，步长是step

        [10, 20, 30]
        [20, 30]
        [10, 20]
        [20, 30]
        [20]
"""
a = [10, 20, 30]
print(a[:])
print(a[1:])
print(a[:2])
print(a[1:3])
print(a[1:6:2])

# 逆序输出 [70, 60, 50, 40, 30, 20, 10]
print([10,20,30,40,50,60,70][::-1])