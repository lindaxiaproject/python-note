"""
 [:]             -- 提取整个字符串
 [start:]         -- 从start索引开始到结尾
 [:end]           -- 从头开始到end-1
 [start:end]      -- 从start到end-1
 [start:end:step] -- 从start提取到end-1,步长是step

 "包头不包尾"

"""

# abcdef
a = "abcdef"
print(a[:])
# cdef
print(a[2:])
# ab
print(a[:2])
# cd
print(a[2:4])
# bd
print(a[1:5:2])