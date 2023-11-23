import re

s = 'hello python'
pattern = r'^hello.*'
print('匹配字符串hello python的结果： \n', re.match(pattern, s))
s = 'hepython'
pattern = r'^hello.*'
# 匹配字符串hepython的结果： None
print('匹配字符串hepython的结果：', re.match(pattern, s))
