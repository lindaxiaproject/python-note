import re

print('---------手机号码-----------')
s = '13456788789'
pattern = '\d\d\d\d\d\d\d\d\d\d\d'  # 匹配手机号
print('匹配手机号码：', re.match(pattern, s))
pattern = '1[35789]\d\d\d\d\d\d\d\d\d'  # 匹配手机 号
print('匹配手机号码：', re.match(pattern, s))
