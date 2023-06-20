import pymysql


def selectTest():
    db = pymysql.connect(host='192.168.0.80',port=3306,user='student',password='student123',db='DHchoi',charset='UTF8')
    try:
        with db.cursor() as cursor:
            sql = "select * from test1"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                print(row[0],row[1])
            return result
    except Exception as e:
        print(e)
    finally:
         db.close()