import re

pattern=r'\w+'
s='first 1 second 2 third 3'
o=re.findall(pattern,s)
# ['first', '1', 'second', '2', 'third', '3']
print(o)


pattern=r'\w+'
s='first 1 second 2 third 3'
o=re.finditer(pattern,s)
print(o)
for i in o:
    """
    first
    1
    second
    2
    third
    3
    """
    print(i.group())