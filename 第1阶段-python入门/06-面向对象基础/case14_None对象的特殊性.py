"""

    与C和JAVA不同，  python中是没有NULL的，取而代之的是None
        None 是一个特殊的常量，表示变量没有指向任何对象。
        在Python中，None本身实际上也是对象，有自己的类型
        你可以将None 赋值给任何变量，但我们不能创建NoneType类型的对象

    None不是False， None不是0， None不是空字符串。None和任何其他的数据类型比较永远返回False
"""

obj = None
obj2 = None


'''
<class 'NoneType'>
4380294896
4380294896
4380294896
'''
print(type(None))
print(id(None))
print(id(obj))
print(id(obj2))