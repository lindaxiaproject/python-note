import re

pattern = '\s'  # 匹配空白字符,即空格（\n,\t）
s = ' '
# 匹配字符 ：  <re.Match object; span=(0, 1), match=' '>
print('匹配字符' ' ： ', re.match(pattern, s))
s = '\t'
# 匹配字符\t：  <re.Match object; span=(0, 1), match='\t'>
print('匹配字符\\t： ', re.match(pattern, s))
s = '\n'
# 匹配字符\n：  <re.Match object; span=(0, 1), match='\n'>
print('匹配字符\\n： ', re.match(pattern, s))
s = '_'
# 匹配字符_：  None
print('匹配字符_： ', re.match(pattern, s))
