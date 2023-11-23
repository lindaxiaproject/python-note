import re

print('-----{m}重复m次---------')
pattern='\d{3}'  #出现m次
s='123abc'
print('pattern为\\d{3}匹配123abc结果：' ,re.match(pattern,s))
pattern='\d{4}'  #出现m次
# pattern为\d{4}匹配123abc结果： None
print('pattern为\\d{4}匹配123abc结果：' ,re.match(pattern,s))
print('-----{m,}至少m次---------')
s='1234567abc'
pattern='\d{3,}'  #出现大于m次尽可能满足的都返回
print('pattern为\\d{3,}匹配1234567abc结果： \n',re.match(pattern,s))
print('-----{m,n}重复m到n次---------')
pattern='\d{2,4}'  #出现m到n次
print('pattern为\\d{2,4}匹配1234567abc结果： \n',re.match(pattern,s))