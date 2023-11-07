#encoding=utf-8
import salary


'''

    本模块用来计算公司员工的薪资

    根据传入的月薪，计算出年薪
    :param monthSalary: 月薪
    :return: 年薪
'''
# print(salary.__doc__)
# print(salary.yearSalary.__doc__)


# 测试代码
if __name__ == "__main__":
    print(salary.yearSalary.__doc__)
    print(salary.yearSalary(30000))

