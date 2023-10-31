"""
输出结果：
    True
    4377791088
    4377791088
    True
    True
"""
a = "aabbcc"
b = "aabbcc"
print(a is b)
print(id(a))
print(id(b))
print(a == b)
print("ab" in b)