data = {'a':1, 'b':2, 'c':3}
# 字典数据: {'a': 1, 'b': 2, 'c': 3}
print('字典数据:', data)
# items: dict_items([('a', 1), ('b', 2), ('c', 3)])
print('items:', data.items())
# values: dict_values([1, 2, 3])
print('values:', data.values())
# keys: dict_keys(['a', 'b', 'c'])
print('keys:', data.keys())

# 新特性
keys = data.keys()
items = data.items()
values = data.values()
# mapping-keys: {'a': 1, 'b': 2, 'c': 3}
print("mapping-keys:", keys.mapping)
# mapping-values: {'a': 1, 'b': 2, 'c': 3}
print("mapping-items:", items.mapping)
# mapping-values: {'a': 1, 'b': 2, 'c': 3}
print("mapping-values:", values.mapping)