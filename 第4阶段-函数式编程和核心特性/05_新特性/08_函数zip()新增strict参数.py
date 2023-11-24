keys = ['one','two','three','four']
values = [1,2,3,4,5]
#旧版本
# {'one': 1, 'two': 2, 'three': 3, 'four': 4}
print(dict(zip(keys,values)))
#新版本
# ValueError: zip() argument 2 is longer than argument 1
print(dict(zip(keys,values,strict=True)))