"""
     列表属于可变序列，可以任意修改列表中的元素。
     元组属于不可变序列，不能修改元组中的元素。
        了解：元组的创建和删除，元素的访问和计数即
"""

""" 元组的创建 
        1.通过()创建元组
            通过()创建元组。小括号可以省略。
            如果元组只有一个元素，则必须后面加逗号。
        2.通过tuple()创建元组
 """
a = (10, 20 , 30)
b = 40,50,60
c = (100, )

# <class 'tuple'>
print(type(a))
# <class 'tuple'>
print(type(b))
# <class 'tuple'>
print(type(c))

# 创建一个空元组对象
aa = tuple()
print(aa)
bb = tuple("abc")
# ('a', 'b', 'c')
print(bb)
cc = tuple(range[3])
print(cc)
dd = tuple([1,2,3,4])
print(dd)
