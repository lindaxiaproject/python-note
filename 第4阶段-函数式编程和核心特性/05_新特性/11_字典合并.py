

dic1= {'name':'lindaxia'}
dic2= {'age':18}
# 旧版本
dic1.update(dic2)
# {'name': 'lindaxia', 'age': 18}
print(dic1)

# 新版本
dic3 = dic1 | dic2
# {'name': 'lindaxia', 'age': 18}
print(dic3)

dic1 |= dic2
# 等价于dict1 = dict1 | dict2
# {'name': 'lindaxia', 'age': 18}
print(dic1)