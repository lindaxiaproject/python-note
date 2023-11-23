import re

pattern = r'.*\bab'
# ab左边界的情况
v = re.match(pattern, '123 abr')
print(v)

pattern = r'.*ab\b'
# ab为右边界的情况
v = re.match(pattern, 'wab')
print(v)

# ab不为左边界
pattern = r'.*\Bab'
v = re.match(pattern, '123 abr')
# None
print(v)
# ab不为右边界
pattern = r'.*ab\B'
v = re.match(pattern, 'wab')
# None
print(v)
