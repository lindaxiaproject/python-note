# coding=utf-8
from multiprocessing import Process, current_process
from multiprocessing import Manager


def func(name, m_list, m_dict):
    m_dict['name'] = '林大侠'
    m_list.append('你好')

"""
    ['Hello!!', '你好']
    {'name': '林大侠'}
"""
if __name__ == "__main__":
    with Manager() as mgr:
        m_list = mgr.list()
        m_dict = mgr.dict()
        m_list.append('Hello!!')
        # 两个进程不能直接互相使用对象，需要互相传递
        p1 = Process(target=func, args=('p1', m_list, m_dict))
        p1.start()
        p1.join() # 等p1进程结束，主进程继续执行
        print(m_list)
        print(m_dict)
