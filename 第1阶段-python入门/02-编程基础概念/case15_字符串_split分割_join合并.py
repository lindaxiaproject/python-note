import time

a = "I love u"
b = a.split("v")
# 输出结果为：['I lo', 'e u']
print(b)

c = ['aa', 'bb', 'cc']
d = "***".join(c)
# 输出结果为：aa***bb***cc
print(d)

"""
    拼接字符串方式
        join连接方式的运算效率更高
    
    输出结果：
        +连接方式的运算时间：   0.08526206016540527
        join连接方式的运算时间：0.04516911506652832
"""
time1 = time.time()
aa = ""
for i in range(1000000):
    a += "sxt"
time2 = time.time()
print("+连接方式的运算时间：" + str(time2 - time1))

time3 = time.time()
li = []
for j in range(1000000):
    li.append("sxt")
aaa = "".join(li)
time4 = time.time()
print("join连接方式的运算时间：" + str(time4 - time3))
