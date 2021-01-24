# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask

mysql_config = {
    "user": "bi",
    "password": "Biplatform-123456",
    "database": "datahouse",
    "host": "127.0.0.1",
    "port": 3306
}
engine = create_engine('mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8'.format(mysql_config['user'],
                                                                                   mysql_config['password'],
                                                                                   mysql_config['host'],
                                                                                   mysql_config['port'],
                                                                                   mysql_config['database']),
                       pool_size=100,
                       max_overflow=0)

app = Flask(__name__)


@app.route("/")
def hello():
    DBSession = sessionmaker(engine)
    session = DBSession()
    try:
        data = session.execute("SELECT COUNT(*) FROM `zhongzhao_bid_company_agency`")
        a = data.fetchall()
        print(a)
    except Exception as e:
        raise
    finally:
        session.close()
    return "hello world"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
