import random

"""
    列表的遍历
"""

# 20
# 10
# 30
# 40
a = [20, 10, 30, 40]
for obj in a:
    print(obj)

"""
    复制列表所有的元素到新列表对象   
"""
list1 = [30, 40, 50]
list2 = list1
# [30, 40, 50]
print(list2)

list11 = [30, 40, 50]
list12 = [] + list11
# [30, 40, 50]
print(list12)

"""
    列表排序：降序、升序
"""
aa = [20, 10, 30, 40]
print(id(aa))
aa.sort()
# [10, 20, 30, 40]
print(aa)

bb = [20, 10, 30, 40]
bb.sort(reverse=True)
# [40, 30, 20, 10] 降序
print(bb)

random.shuffle(bb)
# [10, 30, 40, 20] 打乱顺序
print(bb)

"""
    建新列表的排序： 通过内置函数sorted()进行排序，这个方法返回新列表， 不对原列表做修改。
"""
cc = [20, 10, 30, 40]
print(id(cc))
# 默认升序
dd = sorted(cc)
# [10, 20, 30, 40]
print(dd)

ccc = [20, 10, 30, 40]
print(id(ccc))
# 降序
ddd = sorted(cc, reverse=True)
# [40, 30, 20, 10]
print(ddd)

"""
    reversed()返回迭代器:支持进行逆序排列
    使用list(c)进行输出，发现只能使用一次。
        第一次 输出了元素，第二次为空
        因为迭代对象在第一次时已经遍历结束了，第二次不能再使用。
"""
ff =  [20,10,30,40]
ee = reversed(ff)
# <list_reverseiterator object at 0x104797f70>
print(ee)
# [40, 30, 10, 20]
print(list(ee))

"""
    列表相关的其他内置函数汇总 max和min
"""
kk = [3, 10, 20, 15, 9]
print(max(kk))
print(min(kk))
print(sum(kk))

a = [
["高小一",18,30000,"北京"],
["高小二",19,20000,"上海"],
["高小五",20,10000,"深圳"],
]