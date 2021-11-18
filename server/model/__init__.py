import pymysql
from dbutils.pooled_db import PooledDB
import logging
from functools import wraps
from settings import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB

logger = logging.getLogger(__name__)

class mysql_conn(object):
    config = {
        'creator': pymysql,
        'host': MYSQL_HOST,
        'port': MYSQL_PORT,
        'user': MYSQL_USER,
        'password': MYSQL_PASSWORD,
        'db': MYSQL_DB,
        'charset': 'utf8',
        'maxconnections': 70,
        'cursorclass': pymysql.cursors.DictCursor
    }
    pool = PooledDB(**config)

    def __enter__(self):
        self.conn = mysql_conn.pool.connection()
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, type, value, trace):
        self.cursor.close()
        self.conn.close()

    def __call__(self, func):
        @wraps(func)
        def wrapped_(*args, **kwargs):
            with mysql_conn() as db:
                kwargs['db'] = db
                result = func(*args, **kwargs)
            return result
        return wrapped_


@mysql_conn()
def init_database(*args, **kwargs):
    user_table = '''
    CREATE TABLE IF NOT EXISTS users(
        ID INT  PRIMARY KEY AUTO_INCREMENT,
        name varchar(20) NOT NULL,
        password varchar(50) NOT NULL,
        token varchar(255),
        expTime datetime,
        create_time datetime DEFAULT CURRENT_TIMESTAMP,
        update_time datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
    '''
    db = kwargs['db']
    db.cursor.execute(user_table)
    db.cursor.execute("INSERT INTO users(name, password) values('admin', 'd033e22ae348aeb5660fc2140aec35850c4da997')")
    db.conn.commit()
    