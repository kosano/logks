from model import mysql_conn
import arrow
import time
import hashlib


class Users(object):

    @mysql_conn()
    def authenticate(self, *args, **kwargs):
        if kwargs.get('token'):
            return self.token_authenticate(**kwargs)
        else:
            return self.pwd_authenticate(**kwargs)

    def token_authenticate(self, token, **kwargs):
        db = kwargs['db']
        _SQL = "SELECT id FROM users WHERE token='%s' AND expTime >= STR_TO_DATE('%s', '%Y-%m-%d %H:%i:%s')"
        now = arrow.now().format('YYYY-MM-DD HH:mm:ss')
        db.cursor.execute(_SQL, (token, now))
        result = db.cursor.fetchone()
        if not result:
            raise Exception('Authentication error, login failed.')
        return result

    def pwd_authenticate(self, user, password, **kwargs):
        db = kwargs['db']
        _SQL = "SELECT id, token FROM users WHERE user='%s' AND password='%s'"
        db.cursor.execute(_SQL, (user, password))
        result = db.cursor.fetchone()
        if not result:
            raise Exception('Authentication error, login failed.')
        if result and not result[1]:
            return self._generate_token(db=db, user=user, uid=result[0], **kwargs)
        return result[1]

    def _generate_token(self, db, user, uid, expire=2592000):
        _key = "daajdkn131"
        _str = f'{_key}{user}{int(time.time())+expire}'
        token = hashlib.sha256(_str.encode('utf-8')).hexdigest()
        _SQL = "UPDATE users set token='%s',expTime=STR_TO_DATE('%s', '%Y-%m-%d %H:%i:%s') where id=%d"
        db.cursor.execute(_SQL, (token, arrow.now().shift(
            days=30).format('YYYY-MM-DD HH:mm:ss'), uid))
        db.cursor.commit()
        return token
