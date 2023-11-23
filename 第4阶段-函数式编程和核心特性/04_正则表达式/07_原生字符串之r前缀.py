import re


s = r'\n123'
print(s)

# 目标字符串
s = '\\n123'
pattern = '\\n\d{3}'
print(re.match(pattern,s))  # 返回No

# 如果想匹配两个反斜杠需要使用两个反斜杠作为转义,即正则中要写四个反斜杠
pattern = '\\\\n\d{3}'
# <re.Match object; span=(0, 5), match='\\n123'>
print(re.match(pattern,s))

pattern = '\\\\n\d{3}'
# <re.Match object; span=(0, 5), match='\\n123'>
print(re.match(pattern,s))

#使用原生字符串r比较方便
pattern = r'\\n\d{3}'
# <re.Match object; span=(0, 5), match='\\n123'>
print(re.match(pattern,s))

