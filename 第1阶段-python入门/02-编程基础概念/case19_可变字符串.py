import io
"""
    应用场景：需要频繁修改的字符串
"""
s = "abcdefghijklmn"
sio = io.StringIO(s)
# <_io.StringIO object at 0x104d0fe20>
# <_io.StringIO object at 0x101033e20>
# <_io.StringIO object at 0x104fd3e20>
print(sio)
# abcdefghijklmn
print(sio.getvalue())

# 指针到索引3这个位置
sio.seek(3)
sio.write("****")
# abc****hijklmn
print(sio.getvalue())