"""
    while、for循环可以附带一个else语句（可选）。如果for、while语句没有被break语句结束，则会执行else子句，否则不执行。
        while  条件表达式：
            循环体
        else:
            语句块

        或者：

        for  变量  in  可迭代对象：
            循环体
        else:
            语句块
"""

# 员工一共4人。录入这4位员工的薪资。全部录入后，打印 提示“您已经全部录入4名员工的薪资”。
# 最后，打印输出录入的薪资和平均薪资

"""
    请您输入一共4名员工的薪资（按Q或q中途结束）:111
    请您输入一共4名员工的薪资（按Q或q中途结束）:1432
    请您输入一共4名员工的薪资（按Q或q中途结束）:8888
    请您输入一共4名员工的薪资（按Q或q中途结束）:122222
    您已经全部录入4名员工的薪资
    录入薪资：  [111.0, 1432.0, 8888.0, 122222.0]
    平均薪资33163.25
"""
salarySum = 0
salarys = []
for i in range(4):
    s = input("请您输入一共4名员工的薪资（按Q或q中途结束）:")
    if s.upper() == 'Q':
        print("录入结束，退出")
        break;
    if float(s) < 0:
        continue
    salarys.append(float(s))
    salarySum += float(s)
else:
    print("您已经全部录入4名员工的薪资")
print("录入薪资： ", salarys)
print("平均薪资{0}".format(salarySum/4))