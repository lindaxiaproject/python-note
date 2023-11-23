import re


s='first123 line'
regex=re.compile(r'\w+') #匹配至少一个字母或数字
m=regex.match(s)
# first123
print(m.group())
# s 的开头是 "f", 但正则中限制了开始为 i 所以匹配失 败
regex = re.compile("^i\w+")
# None
print(regex.match(s))