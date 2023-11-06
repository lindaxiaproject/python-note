"""
    浅拷贝
         Python拷贝一般都是浅拷贝。
         浅拷贝：拷贝时，拷贝源对象，但对象包含的子对象内容不拷贝。

    深拷贝
        使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象。
        深拷贝：拷贝时，拷贝源对象，也递归拷贝对象中包含的子对象


"""

import copy

class MobilePhone:
    def __init__(self,cpu):
        self.cpu = cpu

class CPU:
    pass

c = CPU()
m = MobilePhone(c)


'''

----浅拷贝-------
m： 4347821744
m2： 4347820736
m的cpu： 4347822032
m2的cpu： 4347822032
----深拷贝--------
m： 4347821744
m3： 4347813056
'''
print("----浅拷贝-------")
m2 = copy.copy(m)   # m2是新拷贝的另一个手机对象
print("m：",id(m))
print("m2：",id(m2))
print("m的cpu：",id(m.cpu))
print("m2的cpu：",id(m2.cpu))   # m2和m拥有了一样的cpu对象


print("----深拷贝--------")
m3 = copy.deepcopy(m)
print("m：",id(m))
print("m3：",id(m3))