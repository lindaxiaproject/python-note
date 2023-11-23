import re

#pattern = '\d'  # 匹配数字,即0-9
pattern = '\D'  # 匹配数字,即0-9
s = '9'
# 匹配数字9：  <re.Match object; span=(0, 1), match='9'>
print('匹配数字9： ', re.match(pattern, s))
s = '4'
# 匹配数字4：  <re.Match object; span=(0, 1), match='4'>
print('匹配数字4： ', re.match(pattern, s))
s = 'a'
# 匹配字符a：  None
print('匹配字符a： ', re.match(pattern, s))
s = '_'
# 匹配字符_：  None
print('匹配字符_： ', re.match(pattern, s))
