"""
    文件操作：
        一个完整的程序一般都包括数据的存储和读取；
    文本文件和二进制文件
        （1）文本文件
            文本文件存储的是普通“字符”文本，python默认为 unicode 字符集 （两个字节表示一个字符，最多可以表示：65536个），可以使用记事本程序打开。
        （2）二进制文件
            二进制文件把数据内容用“字节”进行存储，无法用记事本打开。必须使用专用的软件解码。常见的有 MP4视频文件、MP3音频文件、JPG图片、doc文档等等。

    文件操作相关模块：
        io模块：文件流的输入和输出操作 input output
        os模块：基本操作系统功能，包括文件操作
        glob模块：查找符合特定规则的文件路径名
        fnmatch模块：使用模式来匹配文件路径名
        fileinput模块：处理多个输入文件
        filecmp模块：用于文件的比较
        csv模块：用于csv文件处理
        pickle和cPickle：用于序列化和反序列化
        xml包：用于XML数据处理
        bz2、gzip、zipfile、zlib、tarfile：用于处理压缩和解压缩文件（分别对应不同的算法）

    创建文件对象open()
        open() 函数用于创建文件对象，"open(文件名[,打开方式])"

        打开方式：
            r:读 read模式
            w:写 write模式。如果文件不存在则创建；如果文件存在，则重写新内容；
            a:追加append模式。如果文件不存在则创建；如果文件存在，则在文件末尾追加内容
            b:二进制binary模式（可与其他模式组合使用）
            +:读、写模式（可与其他模式组合使用）

    文本文件的写入（3步骤）：
        创建文件对象
        写入数据
        关闭文件对象


"""

# (1)文本写入操作简单测试[追加append模式。如果文件不存在则创建；如果文件存在，则在文件末尾追加内容]
# ----文本写入操作简单测试----hello world!!!
f = open("/Users/linhong/PycharmProjects/python-note/file/02-file-test.txt", "a")
f.write("hello world!!!")

# (2)文本写入操作简单测试[write模式。如果文件不存在则创建；如果文件存在，则重写新内容；]
with  open(r"/Users/linhong/PycharmProjects/python-note/file/02-file-test.txt", "w") as f:
    f.write("hello world!!!!!!")

