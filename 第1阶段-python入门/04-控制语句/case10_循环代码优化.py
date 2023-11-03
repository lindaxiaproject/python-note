import time

start = time.time()
for i in range(1000):
    result = []
    for j in range(10000):
        c = i * 1000
        # result =  result + (c + j * 100)
        result.append(c + j * 100)
end = time.time()
# 耗时： 1.0013229846954346
print("耗时： {0}".format((end - start)))

""" 进行循环优化 """
start2 = time.time()
for i in range(1000):
    result = []
    c = i * 1000
    for j in range(10000):
        result.append(c + j * 100)
end2 = time.time()
# 耗时： 0.9055581092834473
print("耗时： {0}".format((end2 - start2)))
