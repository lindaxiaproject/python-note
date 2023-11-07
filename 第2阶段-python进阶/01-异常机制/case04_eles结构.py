
'''
    请输入被除数：9
    请输入除数：3
    3.0
    除的结果是： 3.0


    请输入被除数：9
    请输入除数：0
    float division by zero

'''
try:
    a = input("请输入被除数：")
    b = input("请输入除数：")
    c = float(a) / float(b)
    print(c)
except BaseException as e:
    print(e)
else:
    print("除的结果是：", c)