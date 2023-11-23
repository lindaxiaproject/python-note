import re
print('------*匹配零次或多次--------')
pattern='\d*'  #0次或多次
s='123abc'
print('匹配123abc： ' ,re.match(pattern,s))
s='abc'  #这时候不是None而是''
print('匹配abc： ' ,re.match(pattern,s))
print('-----+匹配一次或多次---------')
pattern='\d+'  #1次或多次
s='123abc'
print('匹配123abc： ' ,re.match(pattern,s))
s='abc'  #这时候是None
print('匹配abc： ' ,re.match(pattern,s))
print('-----?匹配一次或零次---------')
pattern='\d?'  #0次或1次
s='123abc'
print('匹配123abc： ' ,re.match(pattern,s))
s='abc'  #这时候是空
print('匹配abc：',re.match(pattern,s))