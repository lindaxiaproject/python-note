import re

m = re.search('abc', 'abcdefg')
# <re.Match object; span=(0, 3), match='abc'>
print(m)
# abc
print(m.group())


# 进行文本模式匹配，匹配失败，match方法返回None
m = re.match('love', 'I love you')
if m is not None:
    print(m.group())
# match运行结果： None
print('match运行结果：', m)
# 进行文本模式搜索，
m = re.search('love', 'I love you')
if m is not None:
    # love
    print(m.group())
print('search的运行结果：', m)
