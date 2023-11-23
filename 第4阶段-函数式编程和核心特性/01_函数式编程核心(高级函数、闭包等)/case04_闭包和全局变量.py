

"""
    需求：实现变量a自增
        通过全局变量，可以实现，但是会污染其它程序
"""
a = 10
def add():
    global a
    a +=1
    print("a:", a)

def print_ten():
    if a==10:
        print("ten!")
    else:
        print("全局变量a，不等于10")
'''
    a: 11
    a: 12
    a: 13
    全局变量a，不等于10
'''
add()
add()
add()
print_ten()