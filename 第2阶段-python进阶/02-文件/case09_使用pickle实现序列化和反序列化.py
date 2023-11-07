"""
    序列化：
        将对象转化成“串行化”数据形式，存储到硬盘或通过网络传输到其他地方。
    反序列化：
        是指相反的过程，将读取到的“串行化数据”转化成对象。

    使用pickle模块中的函数，实现序列化和反序列操作

    pickle.dump(obj, file)
        obj 就是要被序列化的对象，
        file 指的是存储的文件

    pickle.load(file)
        从 file 读取数据，反序列化成对象
"""
import  pickle

# 将对象序列化到文件中(二进制)
with open("/Users/linhong/PycharmProjects/python-note/file/pickle-data.dat","wb") as f:
    name = "林大侠"
    age = 18
    score = [100, 99, 98]
    resume ={'name':name,'age':age, 'score':score}
    pickle.dump(resume, f)

# 将获得的数据反序列化成对象
with open("/Users/linhong/PycharmProjects/python-note/file/pickle-data.dat","rb") as f:
    resume2 = pickle.load(f)
    # {'name': '林大侠', 'age': 18, 'score': [100, 99, 98]}
    print(resume2)

