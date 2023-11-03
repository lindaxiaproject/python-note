"""
多分支选择结构的语法格式如下：
    if 条件表达式1 :
        语句1/语句块1
    elif 条件表达式2:
        语句2/语句块2

    ...
    elif 条件表达式n :
        语句n/语句块n
    [else:
        语句n+1/语句块n+1
    ]
注意：使用中括号 [ ] 通常表示可选，非必选。
"""

""" 方法1  （使用完整的条件表达） """
# score = int(input("请输入分数: "))
score = 80
grade = ""
if(score < 60):
    grade = "不及格"
if(60 <= score < 80):
    grade = "及格"
if(80 <= score < 90):
    grade = "良好"
if(90 <= score < 100):
    grade = "优秀"
# 请输入分数: 80
# 分数是80,等级是良好
print("分数是{0},等级是{1}".format(score,grade))

"""方法2 利用多分支结构"""
score = int(input("请输入分数: "))
grade = ""
if(score < 60):
    grade = "不及格"
elif(score < 80):
    grade = "及格"
elif(score < 90):
    grade = "良好"
elif( score < 100):
    grade = "优秀"
# 请输入分数: 80
# 分数是80,等级是良好
print("分数是{0},等级是{1}".format(score,grade))


"""已知点的坐标(x,y)，判断其所在的象限"""
x = int(input("请输入x坐标:"))
y = int(input("请输入y坐标:"))
if (x==0 and y==0):
    print("原点")
elif(x == 0):
    print("y轴")
elif(y == 0):
    print("x轴")
elif(x > 0 and y > 0):
    print("第1象限")
elif(x < 0 and y > 0):
    print("第2象限")
elif(x < 0 and y < 0):
    print("第3象限")
else:
    print("第4象限")