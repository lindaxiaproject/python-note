import re

s='first 11 second 22 third 33'
# 按数字切分
# ['first ', ' second ', ' third ', '']
print(re.split(r'\d+',s))
# maxsplit 参数限定分隔的次数，这里限定为1，也就是只 分隔一次
# ['first ', ' second 22 third 33']
print(re.split(r'\d+',s,1))