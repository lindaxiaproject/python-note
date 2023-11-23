import re

print('-------\w匹配字母、数字、下划线--------')
pattern = '\w'  # 匹配字母、数字、下划线
s = 'a'
# 匹配字符a：  <re.Match object; span=(0, 1), match='a'>
print('匹配字符a： ', re.match(pattern, s))
s = '_'
# 匹配字符_：  <re.Match object; span=(0, 1), match='_'>
print('匹配字符_： ', re.match(pattern, s))

s = '5'
# 匹配数字5：  <re.Match object; span=(0, 1), match='5'>
print('匹配数字5： ', re.match(pattern, s))
s = 'A'
# 匹配字符A：  <re.Match object; span=(0, 1), match='A'>
print('匹配字符A： ', re.match(pattern, s))
s = '#'
# 匹配字符#：  None
print('匹配字符#： ', re.match(pattern, s))
