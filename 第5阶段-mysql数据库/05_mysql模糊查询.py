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
#编写sql
sql = "select * from t_panel_job_file where job_id=%s"%("'20231017183' or 1=1")
#执行sql
count = cursor.execute(sql)
print("count:",count)
#执行DML时候，会开启一个事务，需要我们主动提交
connection.commit()