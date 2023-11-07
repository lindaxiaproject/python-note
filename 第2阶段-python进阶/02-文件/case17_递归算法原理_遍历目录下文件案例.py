import os
import os.path


# 递归遍历目录树
def my_print_file(path, level):
    child_files = os.listdir(path)
    for file in child_files:
        file_path = os.path.join(path, file)

        print("\t" * level + file_path[file_path.rfind(os.sep) + 1:])
        if os.path.isdir(file_path):
            my_print_file(file_path, level + 1)


my_print_file("/Users/linhong/PycharmProjects/python-note", 0)
