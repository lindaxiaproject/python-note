"""
    "\n" : 行换符
    "\t" : 制表符

    a的输入结果：
        I
        love
        u
    b的输出结果：
        I	love	u

"""
a = 'I\nlove\nu'
print(a)

b = 'I\tlove\tu'
print(b)

"""
 字符串拼接
"""
c = 'lindaxia' + ' study python'
cc = 'lindaxia'' study python'
# lindaxia study python
print(c)
# lindaxia study python
print(cc)

"""
    字符串赋值
"""
d = "love"*8
# 输出结果：lovelovelovelovelovelovelovelove
print(d)


# 以制表符结尾，即不进行换行
# hello	hello2
print("hello", end="\t")
print("hello2")

"""
    输出结果：
        请输入名字：lindaxia
        请输入年薪: 100
        名字：lindaxia
        年薪：1200
"""
name = input("请输入名字：")
salary = input("请输入年薪: ")
print("名字：" + name)
print("年薪：" + str((int(salary)*12)))