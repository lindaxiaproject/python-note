import re
pattern='[A-Za-z_][0-9A-Za-z_]*'
print('pattern为[A-Za-z_][0-9A-Za-z_]*')
s='a'
print('匹配变量名a的结果：' ,re.match(pattern,s))
s='ab'
print('匹配变量名ab的结果：' ,re.match(pattern,s))
s='_ab'
print('匹配变量名_ab的结果：' ,re.match(pattern,s))
s='2ab'
# 匹配变量名2ab的结果： None
print('匹配变量名2ab的结果：' ,re.match(pattern,s))


print('pattern为[A-Za-z_]\w*')
pattern='[A-Za-z_]\w*'
s='a'
print('匹配变量名a的结果：' ,re.match(pattern,s))
s='ab'
print('匹配变量名ab的结果：' ,re.match(pattern,s))
s='_ab'
print('匹配变量名_ab的结果：' ,re.match(pattern,s))
s='2ab'
# 匹配变量名2ab的结果： None
print('匹配变量名2ab的结果：' ,re.match(pattern,s))