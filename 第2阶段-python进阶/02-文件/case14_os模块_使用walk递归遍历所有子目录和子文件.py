"""
    walk()递归遍历所有文件和目录

    os.walk()  方法是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情。
        os.walk(top[, topdown =True[, onerror =None[, follow links =False]]])
            top :是要遍历的目录。
            topdown ：可选, True，先遍历top目录再遍历子目录。
        返回三元组（root、dirs、files ）
            root：当前正在遍历的文件夹本身
            dirs：一个列表，该文件夹中所有的目录的名字
            files：一个列表，该文件夹中所有的文件的名字
"""
import os

path = os.getcwd()
list_files = os.walk(path, topdown=False)

for root,dirs,files in list_files:
    for name in files:
        print(os.path.join(root,name))
    for name in dirs:
        print(os.path.join(root,name))
