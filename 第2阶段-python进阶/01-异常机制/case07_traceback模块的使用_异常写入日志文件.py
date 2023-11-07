import traceback

# 使用traceback模块打印异常信息
try:
    print("step1")
    num = 1 / 0
except:
    with open("/Users/linhong/Desktop/traceback-test.txt", "a") as f:
        traceback.print_exc(file=f)
