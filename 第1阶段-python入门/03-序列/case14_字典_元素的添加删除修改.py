"""
    给字典新增“键值对”。如果“键”已经存在，则覆盖旧的键值对；如果“键”不存在，则新增“键值对”
"""
a = {'name': 'lindaxia', 'age': 18, 'job': 'programmer'}
a['address'] = '北京西城区'
a['age'] = '12'
# {'name': 'lindaxia', 'age': '12', 'job': 'programmer', 'address': '北京西城区'}
print(a)


"""
    使用update()将新字典中所有键值对全部添加到旧字典对象上。如果key有重复，则直接覆盖
"""
b = {'name': 'lindaxia', 'age': 18, 'job': 'programmer'}
c = {'name':'lindaxia','money':1000,'gender':'男'}
b.update(c)
# {'name': 'lindaxia', 'age': 18, 'job': 'programmer', 'money': 1000, 'gender': '男'}
print(b)

"""
     字典中元素的删除，可以使用 del()方法；或者popitem删除所有键值对；        
     pop()删除指定键值对，并返回对应的“值对象”
"""
bb = {'name': 'lindaxia', 'age': 18, 'job': 'programmer'}
del(bb['name'])
# {'age': 18, 'job': 'programmer'}
print(bb)
bb.pop('age')
# {'job': 'programmer'}
print(bb)

"""
    popitem() ：随机删除和返回该键值对。字典是“无序可变序列”，
    因此没有第一个元素、最后一个元素的概念
    popitem 弹出随机的项，因为字典并没有"最后的元素"或者其他有关顺序的概念
    若想一个接一个地移除并处理项，这个方法就非常有效（因为不用首先获取键的列表）
"""
bbb = {'name': 'lindaxia', 'age': 18, 'job': 'programmer'}
r1 = bbb.popitem()
r2 = bbb.popitem()
# {'name': 'lindaxia'}
print(bbb)