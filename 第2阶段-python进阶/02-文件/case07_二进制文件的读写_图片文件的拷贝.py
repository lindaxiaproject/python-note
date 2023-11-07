"""
    二进制文件的处理流程和文本文件流程一致。首先还是要创建文件 对象，不过，我们需要指定二进制模式，从而创建出二进制文件对
象。例如：
	f = open(r"d:\a.txt", 'wb')   #可写的、重写模式的二进制文件对象
	f = open(r"d:\a.txt", 'ab')   #可写的、追加模式的二进制文件对象
	f = open(r"d:\a.txt", 'rb')   #可读的二进制文件对

"""

# 读取图片文件，实现文件的拷贝
with open("../../file/image/img.png", "rb") as srcFile,  open("../../file/image/img_1.png", "wb") as  destFile:
    for line in srcFile:
        destFile.write(line)
