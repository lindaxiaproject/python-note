"""
    文件对象的属性：
        name:返回文件的名字
        mode:返回文件的打开模式
        closed: 若文件被关闭，则返回True

    文件对象的打开模式:
        r:读模式
        w:写模式
        a:追加模式
        b:二进制模式（可与其它模式组合）
        +：读写模式（可与其它模式组合）

    文件对象的常用方法：
     read([size])：从文件中读取size个字节或字符的内容返回。若省略[size]，则读取到文件末 尾，即一次读取文件所有内容
     readline()：从文本文件中读取一行内容
     readlines()：把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表返回
     write(str)：将字符串str内容写入文件
     writelines(s)：将字符串列表s写入文件文件，不添加换行符
     seek(offset[,whence])
        把文件指针移动到新的位置， offset表示相对于whence的多少个字节的偏量；
            offset ：off为正往结束方向移动，为负往开始方向移动whence不同的值代表不同含义：
                0: 从文件头开始计算（默认值
                1：从当前位置开始计算
                 2：从 文件尾开始计算

    tell()：返回文件指针的当前位置
    truncate([size])：
        不论指针在什么位置，只留下指针前size个字节的内容，其余全部删除；如果 没有传入size，则当指针当前位置到文件末尾内容全部删除

    flush()：把缓冲区的内容写入文件，但不关闭文件
    close()：把缓冲区内容写入文件，同时关闭文件，释放文件对象相关资源


"""
# e.txt的内容是:abcefghljklmn
with open("/Users/linhong/PycharmProjects/python-note/file/e.txt", "r", encoding="utf-8") as f:
    print("文件名是： {0}".format(f.name))  # 文 件名是： e.txt
    print(f.tell())  # 0
    print("读取的内容：{0}".format(str(f.readline()))) #读取的内容：abcdefghijklmn
    print(f.tell())  # 14
    f.seek(3, 0) #把文件指针移动到新的位置， offset表示相对于whence的多少个字节的偏量；
    print("读取的内容：{0}".format(str(f.readline()))) #读取的内容：defghijklmn
'''
文件名是： /Users/linhong/PycharmProjects/python-note/file/e.txt
0
读取的内容：abcefghljklmn
13
读取的内容：efghljklmn
'''