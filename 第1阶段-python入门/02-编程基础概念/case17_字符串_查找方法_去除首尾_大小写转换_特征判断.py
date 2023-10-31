a = '''我是大侠,我在北京kkk科技上班。
我的儿子叫林小侠，他4岁了。我是一个编程教育的普及者，希望影响9000万 学习编程的中国人。
我儿子现在也开始学习编程，希望他18岁的时候可以超过我'''

# 第一次出现指定字符串的位置 字符串"4"，索引从1开始 查询在28
print(a.find("4"))
# 最后一次出现指定字符串的位置 查询在25
print(a.rfind("侠"))
# 指定字符串出现了几次 "3"
print(a.count("编程"))
# 所有字符全是字母或数字
print(a.isalnum())


"""
 大小写转换
   a.capitalize()  产生新的字符串,首字母大写
   a.title()       产生新的字符串,每个单词都首字母 大写
   a.upper()       产生新的字符串,所有字符全转成大写
   a.lower()       产生新的字符串,所有字符全转成小写
   a.swapcase()    产生新的,所有字母大小写转换
   
"""
a = "lindaxia  love  programming, love  JAVA"

# Lindaxia  love  programming, love  java
print(a.capitalize())
# Lindaxia  Love  Programming, Love  Java
print(a.title())
# LINDAXIA  LOVE  PROGRAMMING, LOVE  JAVA
print(a.upper())
# lindaxia  love  programming, love  java
print(a.lower())
# LINDAXIA  LOVE  PROGRAMMING, LOVE  java
print(a.swapcase())


"""
    格式排版(以下三个函数用于对字符串实现排版)
        center()、ljust()、rjust()     
"""

aa = "K8S"
# ***K8S****
print(aa.center(10,"*"))
#    K8S
print(aa.center(10))
# K8S*******
print(aa.ljust(10,"*"))

"""
    isalnum()   是否为字母或数字
    isalpha() 检测字符串是否只由字母组成(含汉字)
    isdigit()   检测字符串是否只由数字组成
    isspace() 检测是否为空白符
    isupper()    是否为大写字母
    islower() 是否为小写字母
"""

# True
print("Python666".isalnum())
# False
print("Python666".isalpha())
# False
print("Python666".isdigit())
# False
print("Python666".isspace())
# False
print("Python666".isupper())
# False
print("Python666".islower())