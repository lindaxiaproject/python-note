import pymysql


class DBUtil:
    config = {
        "host": "192.168.8.121",
        "port": 13306,
        "user": "root",
        "password": "aiquant_mysql",
        "db": "mytest",
        "charset": "utf8"
    }

    def __init__(self):
        self.connection = pymysql.connect(**DBUtil.config)
        self.cursor = self.connection.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    # 插入 修改  删除调用
    def exeDML(self, sql, *args):
        try:
            # 执行sql
            count = self.cursor.execute(sql, args)
            # 提交事务
            self.connection.commit()
            return count
        except Exception as e:
            print(e)
            if self.connection:
                self.connection.rollback()
        finally:
            self.close()

    def query_one(self, sql, *args):
        try:
            # 执行sql
            self.cursor.execute(sql, args)
            # 获取结果集
            return self.cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            self.close()

    def query_all(self, sql, *args):
        try:
            # 执行sql
            self.cursor.execute(sql, args)
            # 获取结果集
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            self.close()


if __name__ == "__main__":
    dbutil = DBUtil()
    sql = "select * from t_panel_job_file"
    emps = dbutil.query_all(sql)
    for e in emps:
        print(e, end="\n")

