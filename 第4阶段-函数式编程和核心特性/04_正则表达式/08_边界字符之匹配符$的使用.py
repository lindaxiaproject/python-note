import re
#匹配qq邮箱， 5-10位
print('未限制结尾'.center(30, '-'))
pattern = '[\d]{5,10}@qq.com'
print('正确的邮箱匹配结果： \n',re.match(pattern,'12345@qq.com'))
print('不正确的邮箱匹配结果： \n',re.match(pattern,'12345@qq.comabc'))

print('限制结尾'.center(30, '-'))
pattern = '[1-9]\d{4,9}@qq.com$'
print('正确的邮箱匹配结果： \n',re.match(pattern,'12345@qq.com'))
print('不正确的邮箱匹配结果： n',re.match(pattern,'12345@qq.comabc'))