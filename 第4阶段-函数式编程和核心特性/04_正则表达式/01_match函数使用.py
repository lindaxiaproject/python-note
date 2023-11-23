import re

pattern = 'hello'
str ='hello world'
result = re.match(pattern, str)
# <re.Match object; span=(0, 5), match='hello'>
print(result)
# 匹配内容 hello
print('匹配内容', result.group())
# (0, 5)
print(result.span())

'''忽略大小写'''
pattern2 = 'hello'
str2 ='Hello world'
result2 = re.match(pattern2, str2, re.I)
# <re.Match object; span=(0, 5), match='Hello'>
print(result2)


pattern3 = 'hello'
str3 ='Hello world hello'
result3 = re.search(pattern3, str3)
# <re.Match object; span=(12, 17), match='hello'>
print(result3)



