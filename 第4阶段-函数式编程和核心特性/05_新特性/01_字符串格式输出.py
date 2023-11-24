#旧版本
name =  '林大侠'
print('公司是：%s'%name)
print('公司是：{}'.format(name))

#新版本
print(f'欢迎加入：{name}')
languages = ['Python','SQL']
print(f'课程包含:{languages[0]},{languages[1]} 等多种开发技术')

#格式化字符串字面值（formatted string literal），可以在字符串常量内使用嵌入的Python表达式。
a = 5
b = 10
print(f'表达式运算的结果：{2*(a+b)}')