import pymysql

host='192.168.0.80'
port= 3306
user='student'
password='student123'
dbname='DHchoi'
charset='utf8'


def connect():
    db = pymysql.connect(
        host=host, 
        port=port,
        user=user,
        password=password,
        db=dbname,
        charset=charset
    )
    return db
def close(db):
    db.close()