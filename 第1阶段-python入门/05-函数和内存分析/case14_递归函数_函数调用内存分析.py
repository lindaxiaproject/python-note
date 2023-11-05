"""
   递归(recursion)是一种常见的算法思路，在很多算法中都会用 到。比如：深度优先搜索（DFS:Depth First Search）等。
   递归的基本思想就是“自己调用自己”
   每个递归函数必须包含两个部分：
    终止条件：表示递归什么时候结束。  一般用于返回值，不再调用自己。
    递归步骤：把第n步的值和第n-1步相关联。
"""

def my_resursion(n):
    print("start:"+ str(n))
    if n == 1:
        print("recursion over!")
    else:
        my_resursion(n -1)
    print("end:"+ str(n))

'''
    start:4
    start:3
    start:2
    start:1
    recursion over!
    end:1
    end:2
    end:3
    end:4
'''
my_resursion(4)

# 使用递归函数计算阶乘（factorial） 5!=5*4*3*2*1
# f(5)
# 5*f(5)-->4*f(3)--> 3*f(2)-->2*f(1)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# 120
print(factorial(5))