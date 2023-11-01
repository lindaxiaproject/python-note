"""
    通过  [键]  获得“值”。若键不存在，则抛出异常。
"""
a = {'name': 'lindaxia', 'age': 18, 'job': 'programmer'}
b = a['name']
# lindaxia
print(b)

"""
    通过get()方法获得“值”。 ❤推荐使用
        指定键不存在，返回None；也可以设定指定键不存在时默认返回的对象。推荐使用get()获取“值对象”
"""
bb = a.get('name')
# lindaxia
print(bb)
cc = a.get('gender', '不存在')
# 返回设置的默认值"不存在"
print(cc)
ccc = a.get('gender')
# None
print(ccc)

"""
    列出所有的键值对
"""
d = a.items()
# dict_items([('name', 'lindaxia'), ('age', 18), ('job', 'programmer')])
print(d)

"""
    列出所有的键，列出所有的值
"""
k = a.keys()
v = a.values()
# dict_keys(['name', 'age', 'job'])
print(k)
# dict_values(['lindaxia', 18, 'programmer'])
print(v)

"""
    len() 键值对的个数
"""
num = len(a)
# 3
print(num)

"""
    检测一个“键”是否在字典中
"""
# True
print("name" in a)
