"""
    break语句可用于while和for循环，用来结束整个循环。
    当有嵌套循环时， break语句只能跳出最近一层的循环。
"""

while True:
    a = input("请出入一个字符(输入Q或q结束):")
    # if a == 'Q' or a = 'q'
    if a.upper() == 'Q':
        print("循环结束，退出!")
        break
    else:
        print(a)

"""
    continue语句用于结束本次循环，继续下一次。
    多个循环嵌套时， continue也是应用于最近的一层循环。
"""

"""
    要求输入员工的薪资，若薪资小于0则重新输入。最后打印
    出录入员工的数量和薪资明细，以及平均薪资
"""
empNum = 0 # 员工数
salarySum = 0 # 录入薪资
salarys = [] # 总发薪资
while True:
    s = input("请输入员工的薪资(按Q或q结束)：")
    if s.upper() == 'Q':
        print("录入结束")
        break
    if float(s) < 0:
        print("无效！继续录入......")
        continue
    print("录入成功！")
    empNum += 1
    salarys.append(float(s))
    salarySum += float(s)

print("员工数{0}".format(empNum))
print("录入薪资：", empNum)
print("总发薪资：", salarySum)

