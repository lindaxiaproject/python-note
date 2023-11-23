import re

s = 'aa|bb|cc'
# match进行匹配
m = re.match(s, 'aa')  # aa满足要求，匹配成功
# aa
print(m.group())

m = re.match(s, 'bb')  # bb满足要求，匹配成功

# bb
print(m.group())

# search查找
m = re.search(s, 'Where is cc')
# cc
print(m.group())


pattern = '[1-9]?\d$|100$'
print(re.match(pattern,'0'))
print(re.match(pattern,'10'))
print(re.match(pattern,'100'))
print(re.match(pattern,'99'))
print(re.match(pattern,'200'))
