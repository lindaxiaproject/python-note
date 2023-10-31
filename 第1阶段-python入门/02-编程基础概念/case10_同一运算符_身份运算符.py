
"""
身份运算符
  a的地址：4379821200
  b的地址：4379821200
  地址是一样，即为同一个对象 True

   is 用于判断两个变量引用对象是否为同一个，即比较对象的地址
   == 用于判断引用变量引用对象的值是否相等，值是否相等
   "is" 比 "==" 的执行效率高
 
   文件模式下，所有数字都会被缓存！！！

"""
a = 30
b = 30
print(id(a))
print(id(b))
# True （比较地址）
print(a is b)
# True （比较值）
print(a == b)

aa = 257
bb = 257
# True （比较地址）文件模式下，所有数字都会被缓存
print(aa is bb)

"""
 成员运算符
"""
aaa = "python"
bbb = "on"
# True （aaa包含了bbb的字符）
print(bbb in aaa)
