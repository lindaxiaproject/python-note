"""
    将字符串 str 当成有效的表达式来求值并返回计算结果。
    eval(source[, globals[, locals]])  - >  value

    	source  ：一个Python表达式或函数 compile() 返回的代码对象
	    globals  ：可选。必须是
	    locals  ：可选。任意映射对象

	val函数 会将字符串当做语句来执行，因此会被注入安全隐患。比如：字符串中含有删除文件的语句。那就麻烦大
"""

# 测试eval()函数

s = "print('abcde')"
'''
    隐患；把字符串当作源码使用
    打印输出: abcde
'''
eval(s)
a = 10
b = 20
c = eval("a+b")
'''
   打印输出: 30
'''
print(c)
dict1 = dict(a=100,b=200)
d = eval("a+b",dict1)