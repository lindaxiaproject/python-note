"""
    shutil模块是python标准库中提供的，主要用来做文件和文件夹的拷 贝、移动、删除等；还可以做文件和文件夹的压缩、解压缩操作。
    os 模块提供了对目录或文件的一般操作。shutil模块作为补充，提供了移动、复制、压缩、解压等操作，这些 os 模块都没有提供。

"""
import shutil
import zipfile

# #copy文件内容
# shutil.copyfile("/Users/linhong/PycharmProjects/python-note/file/csv/csvdata.csv","/Users/linhong/PycharmProjects/python-note/file/csv/csvdatacpoy.csv")

# 实现递归的拷贝文件夹内容(使用 shutil 模块)
#shutil.copytree("/Users/linhong/PycharmProjects/python-note/第1阶段-python入门",
                # "/Users/linhong/PycharmProjects/python-note/file1", ignore=shutil.ignore_patterns("*.html", "*.htm"))


'''将"第1阶段-python入门"文件夹下所有内容压缩到"file"文件夹下 生成ziptest.zip'''
shutil.make_archive("/Users/linhong/PycharmProjects/python-note/file/ziptest","zip","/Users/linhong/PycharmProjects/python-note/第1阶段-python入门")


