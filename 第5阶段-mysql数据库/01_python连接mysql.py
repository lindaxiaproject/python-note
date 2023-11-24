import pymysql

# 获取连接
connection = pymysql.connect(host="192.168.8.121",
                             port=13306,
                             user="root",
                             password="aiquant_mysql",
                             database="mytest",
                             charset="utf8")
# 连接成功，打印对象 <pymysql.connections.Connection object at 0x100ae3040>
print(connection)
# 创建游标
cursor = connection.cursor()
# 编辑sql
sql = "select * from t_panel_job_file"
# 执行sql
cursor.execute(sql)
# 查看结果集
panel_jobs = cursor.fetchall()
# <class 'tuple'> 返回元组信息
print(type(panel_jobs))
# print(panel_jobs)

for panel_job in panel_jobs:
    '''
    ('20231017183140308500048', 'players.csv', '20231017183134176500042', '/home/qe/project_cen/pycharm_project_666/OnlineSyn/userdata/20231017183134176500042/players/players.csv', '1', 'S', '2023-10-17', '2023-10-17 18:31:44', '2023-10-17 18:31:50')
    ('20231017183210022500063', 'card.csv', '20231017183202613500057', '/home/qe/project_cen/pycharm_project_666/OnlineSyn/userdata/20231017183202613500057/card/card.csv', '1', 'S', '2023-10-17', '2023-10-17 18:32:30', '2023-10-17 18:32:40')
    '''
    print(panel_job, end="\n")


