"""
    序列解包可以用于元组、列表、字典。序列解包可以让我们方便的对多个变量赋值。
"""
s = {'name': 'lindaixa', 'age': 18, 'job': 'teacher'}
a, b, c = s
# 默认对键进行操作 name
print(a)
# n a
print(a[0], a[1])

name, age, job = s.items()
# 对键值对进行操作 ('name', 'lindaixa')
print(name)

"""
    表格数据使用字典和列表存储和访问
"""
r1 = {"name" : "林小一", "age" : 18, "salary" : 30000, "city":"北京"}
r2 = {"name" : "林小二", "age" : 19, "salary" : 20000, "city":"上海"}
r3 = {"name" : "林小五", "age" : 20, "salary" : 10000, "city":"深圳"}
tb = [r1, r2, r3]
print(tb)
# 获得第二行的人的薪资 20000
print(tb[1].get("salary"))
"""
遍历输出结果：
        20000
        30000
        20000
        10000
"""
for i in range(len(tb)):
    print(tb[i].get("salary"))
# 深圳
print(tb[2].get("city"))