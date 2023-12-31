"""
  构造方法
    初始化对象需要定义构造函数__init__()方法
    构造方法用于执行"实例对象的初始化工作"，即对象创建后，初始化当前对象的相关属性，无返回值。

    __init__()要点
        名称固定，必须为：__init__()
        第一个参数固定，必须为:self 。self指的就是刚刚创建好的实例对象
        构造函数通常用来初始化实例对象的实例属性，如下代码就是初始化实例属性:name和score


    __init__()方法：
        初始化创建好的对象，初始化指的是：“给实例属性赋值”
        用于创建对象，但我们一般无需重定义该方法
"""
def __init__(self,name,score):
    self.name = name
    self.score = score