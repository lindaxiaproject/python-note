"""
    字典是“键值对”的无序可变序列，字典中的每个元素都是一个“键值 对”，包含：“键对象”和“值对象”。
    1.通过{}、dict()来创建字典对象
    2.过zip()创建字典对象
    3.通过fromkeys创建值为空的字典
"""

a = {'name':'lindaxia','age':18,'job':'programmer'}
b = dict(name='lindaxia',age=18,job='programmer')
a = dict([("name","lindaxia"),("age",18)])
# 空的字典对象
c = {}
# 空的字典对象
d = dict()

# 2.过zip()创建字典对象
k = ['name','age','job']
v = ['gaoqi',18,'teacher']
d = dict(zip(k,v))
# {'name': 'gaoqi', 'age': 18, 'job': 'teacher'}
print(d)

# 3.通过fromkeys创建值为空的字典
f = dict.fromkeys(['name','age','job'])
# {'name': None, 'age': None, 'job': None}
print(f)
