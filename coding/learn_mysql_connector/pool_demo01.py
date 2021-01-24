# -*- coding: utf-8 -*-
from mysql.connector.errors import PoolError
from mysql.connector.pooling import MySQLConnectionPool
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

db = SQLAlchemy()


class UserMySQLConnectionPool(MySQLConnectionPool):

    def __init__(self, *args, **kwargs):
        super(UserMySQLConnectionPool, self).__init__(*args, **kwargs)

    def _set_pool_size(self, pool_size):
        """Set the size of the pool

        This method sets the size of the pool but it will not resize the pool.

        Raises an AttributeError when the pool_size is not valid. Invalid size
        is 0, negative or higher than pooling.CNX_POOL_MAXSIZE.
        """
        if pool_size <= 0 or pool_size > 200:
            raise AttributeError(
                "Pool size should be higher than 0 and "
                "lower or equal to {0}".format(200))
        self._pool_size = pool_size

    def init_pool(self, init_pool_size, **kwargs):
        self.set_config(**kwargs)
        cnt = 0
        while cnt < init_pool_size:
            print("test")
            self.add_connection()
            cnt += 1


class MysqlDriver:

    def __init__(self):
        mysql_config = {
            "user": "root",
            "password": "123456",
            "database": "test",
            "host": "192.168.33.20",
            "port": 3306
        }

        self.connection_pool = UserMySQLConnectionPool(pool_size=5,
                                                       pool_name="datahousepool")
        self.connection_pool.set_config(**mysql_config)
        self.connection_pool.init_pool(init_pool_size=2, **mysql_config)

    def select(self, select_sql, params=None):
        cnx = self.connection_pool.get_connection()
        cursor = cnx.cursor()
        try:
            if params:
                cursor.execute(select_sql, params)
                data = cursor.fetchall()
            else:
                cursor.execute(select_sql)
                data = cursor.fetchall()
            return data
        except Exception as e:
            raise
        finally:
            cursor.close()
            cnx.close()


mysql_driver = MysqlDriver()


@app.route("/")
def hello():
    data = mysql_driver.select("SELECT * FROM `test`")
    print(data)
    return "hello world"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
