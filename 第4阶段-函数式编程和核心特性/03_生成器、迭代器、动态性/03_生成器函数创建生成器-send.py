
def foo():
    print("start")
    i = 0
    while i < 3:
            temp = yield i
            print(f"temp:{temp}")
            i = i +1
    print("end")
# <generator object test at 0x104a41e00>
g = foo()
# # 0
# print(next(g))
# print("*"*20)
# '''
# temp:1000
# 1
# '''
# print(g.send(1000))
# '''
# temp:None
# 2
# '''
# print(next(g))

for a in g:
    print(a)