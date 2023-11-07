"""
    os 模块下常用操作文件的方法
        remove(path)：删除指定的文件
        rename(src,dest)： 重命名文件或目录
        stat(path)： 返回文件的所有属性
        listdir(path)： 返回path目录下的文件和目录列表

    os 模块下关于目录操作的相关方法
        mkdir(path)：创建目录
        makedirs(path1/path2/path3/...):创建多级目录
        rmdir(path): 删除目录
        removedirs(path1/path2...): 删除多级目录
        getcwd(): 返回当前工作目录：  current work dir
        chdir(path): 把path设为当前工作目录
        walk(): 遍历目录树
        sep: 当前操作系统所使用的路径分隔符
"""

import os
#  os 模块：创建、删除目录、获取文件信息等
print(os.name)  # windows-->nt  linux-->posix
print(os.sep)   # windows-->\   linux-->/
print(os.linesep)  # windows-->\r\n linux-->\n
a = '3'
print(a)
print(repr(a))  # repr可以显示数据信息
print(os.stat("case12_os模块_获取文件信息_创建和删除文件夹.py")) # 关于工作目录的操作
print(os.getcwd())  #获得当前工作目录 /Users/linhong/PycharmProjects/python-note/第2阶段-python进阶/02-文件
# os.chdir("/") # 当前的工作目录就变成了/的根目录
os.mkdir("测试创建目录")
os.makedirs("创建多级目录1/多级目录2/多级目录3")
os.rename("测试创建目录", "重命名目录")
dirs = os.listdir("创建多级目录1")
print(dirs)
