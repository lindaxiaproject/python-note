import re

pattern = '.' # 匹配任意1个字符（除了\n）
s = 'a'
# 匹配字符啊a:  <re.Match object; span=(0, 1), match='a'>
print('匹配字符啊a: ', re.match(pattern,s))
s='C'
# 匹配字符C： <re.Match object; span=(0, 1), match='C'>
print('匹配字符C：',re.match(pattern,s))
s='_'
# 匹配字符_： <re.Match object; span=(0, 1), match='_'>
print('匹配字符_：',re.match(pattern,s))
s='\n'
# 匹配字符\n： None
print('匹配字符\\n：',re.match(pattern,s))


