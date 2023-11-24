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
sql = "INSERT INTO t_panel_job_file(file_id, file_name, job_id, file_path, storage_status, sync_status, file_date, create_time, modify_time) " \
      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"

args = ('20231113155447403500263', '工商企业查询年报财务数据表(原文件).csv', '20231113155407638500257',
        '/home/qe/project_cen/pycharm_project_666/OnlineSyn/userdata/20231113155407638500257/工商企业查询年报财务数据表(原文件)/工商企业查询年报财务数据表(原文件).csv',
        '1', 'S', '2023-11-13', '2023-11-13 15:54:51', '2023-11-13 15:54:55')
# 执行sql
count = cursor.execute(sql,args)
print(count)
# 执行DML时，会开启一个事物，需要我们主动提交
connection.commit()