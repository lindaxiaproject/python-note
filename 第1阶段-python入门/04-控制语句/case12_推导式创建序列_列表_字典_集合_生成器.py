"""
    推导式是从一个或者多个迭代器快速创建序列的一种方法。它可以将循环和条件判断结合，从而避免冗长的代码。
"""

"""
    (1)列表推导式生成列表对象
        [表达式  for  item  in 可迭代对象 ]
        或者： {表达式  for  item  in 可迭代对象   if  条件判断}
"""
# [1, 2, 3, 4]
print([x for x in range(1, 5)])
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
print([x * 2 for x in range(1, 20)])
# [10, 20, 30]
print([x * 2 for x in range(1, 20) if x % 5 == 0])
# ['l', 'i', 'n', 'd', 'a', 'x', 'i', 'a']
print([a for a in "lindaxia"])

"""体现了推导式优势"""
a = [x for x in range(1, 10) if x % 2 == 0]
# [2, 4, 6, 8]
print(a)

b = []
for x in range(1, 10):
    if x % 2 == 0:
        b.append(x)
# [2, 4, 6, 8]
print(b)

"""#可以使用两个循环 ,使用zip并行迭代"""
cells = [(row, col) for row, col in zip(range(1, 10), range(1, 10))]
# [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]
print(cells)

"""
    (2)字典的推导式生成字典对象，格式如下：
         {key_expression: value_expression  for  表达式 in  可迭代对象}
         类似于列表推导式，字典推导也可以增加if条件判断、多个for循环。
"""
values = ["北京", "上海", "深圳", "广州"]
cities = {id * 100: city for id, city in zip(range(1, 5), values)}
# 生成字典对象 {100: '北京', 200: '上海', 300: '深圳', 400: '广州'}
print(cities)

# 统计文本中字符出现的次数
my_text = ' i love you, i love sxt, i love lindaxia'
char_count = {c: my_text.count(c) for c in my_text}
# {' ': 9, 'i': 5, 'l': 4, 'o': 4, 'v': 3, 'e': 3, 'y': 1, 'u': 1, ',': 2, 's': 1, 'x': 2, 't': 1, 'n': 1, 'd': 1, 'a': 2}
print(char_count)

"""
    (3)集合推导式生成集合 (集合是没有顺序的！！！)
    {表达式 for item in 可迭代对象} 或  {表达式 for item in 可迭代对象 if 条件判断}
"""
# {99, 36, 72, 9, 45, 81, 18, 54, 90, 27, 63}
print({x for x in range(1, 100) if x % 9 == 0})

"""
    (4)生成器推导式（不直接生成元组）
    一个生成器只能运行1次，第1次迭代可以得到数据，第2次迭代发现数据已经没有了

"""
gnt = (x for x in range(1, 100) if x % 9 == 0)
for x in gnt:
    # 9，18，27，36，45，54，63，72，81，90，99，
    print(x, end='，')
for x in gnt:
    # 无结果
    print(x, end='-')

