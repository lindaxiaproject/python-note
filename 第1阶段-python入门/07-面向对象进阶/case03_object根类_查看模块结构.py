"""
    obejct类是所有类的父类，因此所有的类都有object类的属性和方法。
    dir()查看对象属性
"""

obj = object()

'''
    ----方法 可看作 属性---
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
'__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__']
'''
print(dir(obj))
