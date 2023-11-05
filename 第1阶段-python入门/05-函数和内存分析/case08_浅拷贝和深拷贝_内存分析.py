import copy
"""
    copy(浅拷贝)与deepcopy(深拷贝)

    浅拷贝：
        拷贝对象，但不拷贝子对象的内容，只是拷贝子对象的引用。
    深拷贝（递归拷贝）：
        拷贝对象，并且会连子对象的内存也全部（递归）拷贝一份，对子对象的修改不会影响源对象

"""

def testCpoy():
    ''' 测试浅拷贝 '''
    a = [10, 20, [5, 6]]
    b = copy.copy(a)
    print("a", a)
    print("b", b)
    b.append(30)
    b[2].append(7)
    print("浅拷贝后，修改b....")
    print("a", a)
    print("b", b)
'''
a [10, 20, [5, 6]]
b [10, 20, [5, 6]]
浅拷贝后，修改b....
a [10, 20, [5, 6, 7]]
b [10, 20, [5, 6, 7], 30]
'''
print(testCpoy())


'''
    a [10, 20, [5, 6]]
    b [10, 20, [5, 6]]
    深拷贝后，修改b....
    a [10, 20, [5, 6]]
    b [10, 20, [5, 6, 7], 30]
    
    深拷贝后，子对象不再共享！！！
'''
def testDeepCopy():
    '''测试深拷贝 '''
    a = [10, 20, [5, 6]]
    b = copy.deepcopy(a)
    print("a", a)
    print("b", b)
    b.append(30)
    b[2].append(7)
    print("深拷贝后，修改b....")
    print("a", a)
    print("b", b)
print(testDeepCopy())

