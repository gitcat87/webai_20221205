import pymysql

host='127.0.0.1'
port=3306
user='root'
password='root123'
dbname='DHchoi'
charset='utf8'


def selectRow(idx):
    db = pymysql.connect(
        host=host, port=port,
        user=user, password=password,
        db=dbname, charset=charset
    )
    sql = f'select * from freeboard where idx = {idx}'
    
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchone()
    print(res)
    db.close()
    return res


def select(page):
    db = pymysql.connect(
        host=host,port=port,
        user=user,password=password,
        db=dbname,charset=charset
    )
    
    startrow = (page-1)*3
    # 1페이지면 startrow가 0
    # 2페이지면 startrow가 3
    # 3페이지면 startrow가 6
    
    sql = F'select * from freeboard order by idx desc limit {startrow},5'
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    db.close()
    print(res)
    return res