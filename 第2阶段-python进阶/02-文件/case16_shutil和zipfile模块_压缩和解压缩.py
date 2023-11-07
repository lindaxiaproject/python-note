import shutil
import zipfile

# 压缩:将指定的多个文件压缩到一个zip文件
z = zipfile.ZipFile("/Users/linhong/PycharmProjects/python-note/file/a.zip","w")
z.write("/Users/linhong/PycharmProjects/python-note/file/02-test-aa.txt")
z.write("/Users/linhong/PycharmProjects/python-note/file/02-test-bb.txt")
z.close()

# 解压缩：
z2 = zipfile.ZipFile("/Users/linhong/PycharmProjects/python-note/file/a.zip","r")
z2.extractall("/Users/linhong/PycharmProjects/python-note/file/csv")  #设置解压的地址
z2.close()