"""
    os.path 模块提供了目录相关（路径判断、路径切分、路径连接、文件夹遍历）的操作

        isabs(path)	判断path是否绝对路径
        isdir(path)	判断path是否为目录
        isfile(path)	判断path是否为文件
        exists(path)	判断指定路径的文件是否存在
        getsize(filename)	返回文件的大小
        abspath(path)	返回绝对路径
        dirname(p)	返回目录的路径
        getatime(filename)	返回文件的最后访问时间
        getmtime(filename)	返回文件的最后修改时间
        walk(top,func,arg)	递归方式遍历目录
        join(path,*paths)	连接多个path
        split(path)	对路径进行分割，以列表形式返回
        splitext(path)	从路径中分割文件的扩展名
"""
import os
import os.path

################# 获得目录、文件基本信息 ######################
print(os.path.isabs("../../file/02-test-aa.txt"))  # 是否绝对路径
print(os.path.isdir("../../file/02-test-aa.txt"))  # 是否目录
print(os.path.isfile("../../file/02-test-aa.txt"))  # 是否文件
print(os.path.exists("../../file/02-test-aa.txt"))  # 文件是否存在
print(os.path.getsize("../../file/02-test-aa.txt"))  # 文件大小
print(os.path.abspath("../../file/02-test-aa.txt"))  # 输出绝对
print(os.path.dirname("../../file/02-test-aa.txt"))  # 输出所在目录

######## 获得创建时间、访问时间、最后修改时间 ##########
print(os.path.getctime("../../file/02-test-aa.txt"))  # 返回创建时间
print(os.path.getatime("../../file/02-test-aa.txt"))  # 返回最后访问时间
print(os.path.getmtime("../../file/02-test-aa.txt"))  # 返回最后修改时间

################ 对路径进行分割、连接操作 ####################
path = os.path.abspath("../../file/02-test-aa.txt")
# ('/Users/linhong/PycharmProjects/python-note/file', '02-test-aa.txt')
# 返回元组：目录、文件
print(os.path.split(path))
# ('/Users/linhong/PycharmProjects/python-note/file/02-test-aa', '.txt')
# 返回元组：路径、扩展名
print(os.path.splitext(path))
# aa/bb/cc
# #返回路径
print(os.path.join("aa", "bb", "cc"))

# 列出指定目录下所有的 .py 文件，并输出文件名
# path = os.getcwd()
path = "/Users/linhong/PycharmProjects/python-note/第2阶段-python进阶/02-文件"
file_list = os.listdir(path)
for filename in file_list:
    pos = filename.rfind(".")
    if filename[pos + 1:] == "py":
        print(filename, end="\t")
print("##################")
file_list2 = [filename for filename in os.listdir(path) if filename.endswith(".py")]
'''
['case13_os.path模块_常用方法.py', 'case10_csv文件的读取和写入.py', 
'case12_os模块_获取文件信息_创建和删除文件夹.py', 'case09_使用pickle实现序列化和反序列化.py', 
'case11_os模块_调用操作系统可执行文件_控制台乱码问题.py', 
'case01_file文件操作_操作系统底层关系_写入文件.py', 'case06_文本文件操作_为每行添加行号.py',
 'case08_文件对象的常用属性和方法.py', 'case07_二进制文件的读写_图片文件的拷贝.py',
  'case02_编码知识_解决中文乱码问题.py', 'case04_关闭流_with上下文管理.py',
   'case03_关闭流_finally异常管理.py', 'case05_文本文件的读取.py']
'''
print(file_list2)
