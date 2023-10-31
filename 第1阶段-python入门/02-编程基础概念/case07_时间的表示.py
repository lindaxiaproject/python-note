import time

"""
    time.time() 获取当前时间，返回的值以秒为单位
    
    1698738214
    28312303
    19661
    53
"""
# 精确到秒
b = int(time.time())
# 1698737964
print(b)

# 获取分钟--整除
totalMin = b // 60
print(totalMin)

# 多少天
totalDays = totalMin // (60*24)
print(totalDays)

# 多少年 输入53 从1970年1月1号开始计算
totalYears = totalDays // 365
print(totalYears)
