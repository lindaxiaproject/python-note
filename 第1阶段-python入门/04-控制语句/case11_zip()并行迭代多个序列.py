"""
    通过zip()函数对多个序列进行并行迭代，zip()函数在最短 序列“用完”时就会停止
"""

names = ("林大侠", "林二侠", "林三侠", "林四侠")
ages = (18, 16, 20, 25)
jobs = ("老师", "程序员", "公务员")

"""
输入结果：
    林大侠--18--老师
    林二侠--16--程序员
    林三侠--20--公务员
"""

# for names, ages, jobs in zip(names, ages, jobs):
#     print("{0}--{1}--{2}". format(names, ages, jobs))

# 方式二
for i in range(min(len(names), len(ages), len(jobs))):
    print("{0}--{1}--{2}".format(names[i], ages[i], jobs[i]))
