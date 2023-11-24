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
sql = "update t_panel_job_file set file_name='林大侠修改文件' where file_id='20231113155447403500261'"
# 执行sql
count = cursor.execute(sql)
print(count)
# 执行DML时，会开启一个事物，需要我们主动提交
connection.commit()