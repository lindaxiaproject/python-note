from functools import reduce

sorter1 = sorted([1,3,6,-20,34])
# 升序排列： [-20, 1, 3, 6, 34]
print("升序排列：", sorter1)

sorter2 = sorted([1,3,6,-20,-60], key=abs)
# 自定义排序： [1, 3, 6, -20, -60]
print("自定义排序：", sorter2)

sorter2 = sorted([1,3,6,-20,-60], key=abs, reverse=True)
# 自定义逆序： [-60, -20, 6, 3, 1]
print("自定义逆序：", sorter2)

'''字符串排序依照ASCII'''
sorter3 = sorted(["ABC", "abc", "D", "d"])
# 字符串排序： ['ABC', 'D', 'abc', 'd']
print("字符串排序：", sorter3)

'''字符串排序依照ASCII,忽略大小写'''
sorter4 = sorted(["ABC", "abc", "D", "d"],key=str.lower)
# 忽略字符串大小写排序： ['ABC', 'abc', 'D', 'd']
print("忽略字符串大小写排序：", sorter4)
