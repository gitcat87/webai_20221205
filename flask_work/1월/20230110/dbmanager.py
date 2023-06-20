import pymysql


def saveFiles(ko,en,filename):
    db = pymysql.connect(
        host='192.168.0.80', 
        port=3306, user='student', password='student123', 
        db='DHchoi', charset='utf8')

    # 커서 가져오기
    cursor = db.cursor()

    # SQL 문 만들기
    sql = f'''
            INSERT INTO files
            (ko, en, filename, regdate)
            VALUES
            ('{ko}','{en}','{filename}',NOW());
                    ;
            '''

    # 실행하기
    cursor.execute(sql)

    # DB에 Complete 하기
    db.commit()

    # DB 연결 닫기
    db.close()
    
def selectFiles():
    db = pymysql.connect(
        host='192.168.0.80', 
        port=3306, user='student', password='student123', 
        db='DHchoi', charset='utf8')
    cursor = db.cursor()
    sql = f'''
            SELECT * FROM files
                    
            '''
    cursor.execute(sql)
    res = cursor.fetchall()
    db.close()
    return res