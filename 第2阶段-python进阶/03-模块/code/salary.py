# encoding=utf-8
'''
    本模块用来计算公司员工的薪资
'''
company = "林大侠全栈科技"
def yearSalary(monthSalary):
    '''
    根据传入的月薪，计算出年薪
    :param monthSalary: 月薪
    :return: 年薪
    '''
    return  monthSalary * 12
def daySalary(monthSalary):
    '''
    根据传入的月薪，计算出每天的薪资
    :param monthSalary: 月薪
    :return: 日薪
    '''
    return  monthSalary/22.5