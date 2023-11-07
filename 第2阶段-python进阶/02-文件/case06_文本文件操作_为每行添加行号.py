

# 为文本文件每一行的末尾添加行号

with open("/Users/linhong/PycharmProjects/python-note/file/02-test-bb.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    line2 = [line.rstrip() + "  #" + str(index)+ "\n" for index,line in zip(range(1,len(lines)+1), lines)]
    '''
    ['abcdefg\n', 'java\n', 'python\n']
    ['abcdefg#1  #1\n', 'java#2  #2\n', 'python#3  #3\n']
    '''
    print(lines)
    print(line2)

'''
02-test-bb.txt原内容：
    abcdefg
    java
    python
    
02-test-bb.txt内容：
    abcdefg  #1
    java  #2
    python  #3

'''
with open("/Users/linhong/PycharmProjects/python-note/file/02-test-bb.txt", "w", encoding="utf-8") as f:
    f.writelines(line2)
