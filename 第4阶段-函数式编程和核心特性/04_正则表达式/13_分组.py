import re

pattern = r'(\d+)-(\d{5,8}$)'
v = re.match(pattern,'010-66668888')
# <re.Match object; span=(0, 12), match='010-66668888'>
print(v)
# 010-66668888
print(v.group())
# 010
print(v.group(1))
# 66668888
print(v.group(2))
# ('010', '66668888')
print(v.groups())
# 010
print(v.groups()[0])
# 66668888
print(v.groups()[1])


#匹配合法的网页标签
s = '<html><title>我是标题</title></html>'
# 匹配不合法的网页标签
ss = '<html><title>我是标题</html></title>'
#优化前
pattern = r'<.+><.+>.+</.+></.+>'
print(re.match(pattern,s))
print(re.match(pattern,ss))

#优化后 可以使用分组 \2 表示引用第2个分组 \1表示 引用第1个分组
pattern = r'<(.+)><(.+)>.+</\2></\1>'
print(re.match(pattern,s))
# None
print(re.match(pattern,ss))