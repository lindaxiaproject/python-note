import re

phone = "2004-959-559 # 这是一个国外电话号码"
''' 删除字符串中的 Python注释 '''

num = re.sub(r'#.*$', "", phone)
# 电话号码是:  2004-959-559
print("电话号码是: ", num)
# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
# 电话号码是 :  2004959559
print("电话号码是 : ", num)

''' subn函数的使用'''
result = re.subn(r'\D', "", phone)
# ('2004959559', 15)
print(result)
# 替换的结果： 2004959559
print('替换的结果：', result[0])
# 替换的次数： 15
print('替换的次数：', result[1])
