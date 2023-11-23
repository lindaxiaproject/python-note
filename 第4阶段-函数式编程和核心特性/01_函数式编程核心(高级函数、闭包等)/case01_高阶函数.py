def test():
    print("test function run!!!")

def test03(a, b):
    print(f"test03,{a},{b}")

def test02(func, *args, **kwargs):
    print("test2 function run!!!")
    func(*args, **kwargs)



a = test
'''
    输出结果：
        test function run!!!
        test2 function run!!!
        test function run!!!
        test2 function run!!!
        test03,100,3000
'''
test02(a)
test02(test03,100, 3000)