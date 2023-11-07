"""
    文件的读取一般使用如下三个方法：
    read([size])
        从文件中读取 size 个字符，并作为结果返回。如果没有 size 参数，则读取整个文件。读取到文件末尾，会返回空字符串。
    readline()
        读取一行内容作为结果返回。读取到文件末尾，会返回空字符串
    readlines()
        文本文件中，每一行作为一个字符串存入列表中，返回该列表
"""

# 读取一个文件前4个字符
with open("/Users/linhong/PycharmProjects/python-note/file/02-test-bb.txt", "r", encoding="utf-8") as f:
    s = f.read(4)
    ss = f.read()
    '''
    abcd
    第二次虚读: 
     efg
    java
    python
    '''
    print(s)
    print("第二次虚读: \n", ss)

with open("/Users/linhong/PycharmProjects/python-note/file/02-test-bb.txt", "r", encoding="utf-8") as ff:
    sss = ff.readlines()
    # ['abcdefg\n', 'java\n', 'python\n'] 一次性全部读取
    print(sss)

# 推荐
with open("/Users/linhong/PycharmProjects/python-note/file/02-test-bb.txt", "r", encoding="utf-8") as fff:
    for line in fff:
        '''
        abcdefg
        java
        python
        '''
        print(line, end="")

# 不推荐
with open("/Users/linhong/PycharmProjects/python-note/file/02-test-bb.txt", "r", encoding="utf-8") as ffff:
    while True:
        line = ffff.readline()
        if not line:
            break
        else:
            print(line, end="")
