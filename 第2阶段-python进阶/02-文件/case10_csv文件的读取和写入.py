"""
    csv是逗号分隔符文本格式，常用于数据交换、 Excel文件和数据库数据的导入和导出。
    Python标准库的模块csv提供了读取和写入csv格式文件的对象。
"""
import csv

#  csv.reader 对象于从csv文件读取数据
with open(r"/Users/linhong/PycharmProjects/python-note/file/csv/csvdata.csv") as f:
    a_csv = csv.reader(f) # 创建csv对象 ,它是一个包含所有数据的列表，每一行为一个元素
    headers = next(a_csv)  # 获得列表对象，包含标题行的信息
    print(headers)
    for row in a_csv:
        '''
        ['姓名', '年龄', '职业', '薪水']
        ['林大侠', '18', '程序员', '19999']
        ['刘德华', '29', '演员', '18888']
        '''
        print(row)

# csv.writer对象写一个csv文件
headers = ["工号","姓名","年龄","地址","月薪"]
rows = [("1001","林大侠",18,"北京西城","50000"),("1002","林二侠",19,"北京朝阳 院","30000")]

with open(r"/Users/linhong/PycharmProjects/python-note/file/csv/writer-test.csv", "w") as f:
    b_csv = csv.writer(f) # 创建csv对象
    b_csv.writerow(headers) # 写入一行（标题）
    b_csv.writerows(rows)  # 写入多行（数据）