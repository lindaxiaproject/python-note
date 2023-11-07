"""
    ASCII:
        全称为 American Standard Code for Information Interchange，美国信息交换标准代码，这是世界上最早最通用的单字节编码系统，主要用来显示现代
    英语及其他西欧语言。

    ISO8859-1：
        又称Latin-1 ，是一个8位单字节字符集
        在ASCII编码之上又增加了西欧语言、希腊语、泰语、阿拉伯语、希伯来语对应的文字符号，它是向下兼容ASCII编码。
    GB2312：
        全称为信息交换用汉字编码字符集，是中国于1980年发布,主要用于计算机系统中的汉字处理。
        GB2312  主要收录了6763个汉字、 682个符号。
        GB2312 完全兼容ISO8859-1
    GBK:
        全称为Chinese Internal Code Specification，即汉字内码扩展规范，于1995年 制定。
        它主要是扩展GB2312，在它的基础上又加了更多的汉字，它一共收录了21003个汉字.

    GB18030:
        现在最新的内码字集于2000年发布，并于2001年强制执行，包含了中国大部分少数民族的语言字符，收录汉字数超过70000余个。
        它主要采用单字节、双字节、四字节对字符编码，它是向下兼容GB2312 和 GBK 的，虽然是我国的强制使用标准，但在实际生产中很少用到，用得最多的反而是 GBK 和 GB2312

    Unicode:
        Unicode 编码设计成了固定两个字节，所有的字符都用16位(2^16=65536)表示，包括之前只占8位的英文字符等，所以会造成
    空间的浪费， UNICODE 在很长的一段时间内都没有得到推广应用。
        Unicode 完全重新设计，不兼容 iso8859- 1  ，也不兼容任何其他编码。

    UTF-8:【项目基本会采用这个编码】
        对于英文字母，unicode 也需要两个字节来表示。所以unicode不便于传输和存储。因此而产生了UTF编码，UTF-8全称是(Transformation Format ）。
        完全兼容so8859- 1编码，同时也可以用来表示所有语言的字符。
        不过，UTF编码是不定长编码，每一个字符的长度从1-4个字节不等。其中，英文字母都是用1个字节表示，而汉字使用3个字节。


    中文乱码问题
        windows操作系统默认的编码是GBK ，Linux操作系统默认的编码是UTF-8 。当我们用open()时，调用的是操作系统打开的文件，默认的编码是GBK。
"""

# 测试写入中文 通过指定文件编码解决中文乱码问题
with open(r"/Users/linhong/PycharmProjects/python-note/file/02-test-aa.txt", "w", encoding="utf-8") as f:
    f.write("林大侠\n学python")


"""
    write(a)  ：把字符串 a 写入到文件中
    writelines(b)  ：把字符串列表写入文件中，不添加换行符
"""

# 添加字符串【列表】数据到文件中
f = open(r"/Users/linhong/PycharmProjects/python-note/file/02-test-bb.txt", "w", encoding="utf-8")
s = ["林大侠\n", "java\n", "python\n"]
f.writelines(s)
f.close()