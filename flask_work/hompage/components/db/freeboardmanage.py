import pymysql

host='127.0.0.1'
port=3306
user='root'
password='root123'
dbname='DHchoi'
charset='utf8'

#view페이지에 필요한 내용
#게시판에 행선택을 할거에요
def selectRow(idx):
    db = pymysql.connect(
        host=host,port=port,
        user=user,password=password,
        db=dbname,charset=charset
    )
    sql = f'select * from freeboard where idx = {idx}'
    
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchone()
    db.close()
    return res
    #mysql에 freeboard 데이터에서 모두 선택하세요 근데
    #어디(where)? 변수 idx 값이 ={idx} 인곳 만약 15번째면 15번째 데이터 선택

    
#게시판 아래에서 < 1 2 3 4 5 > 이런 표시 보여주는 곳
def select(page):
    db = pymysql.connect(
        host=host,port=port,
        user=user,password=password,
        db=dbname,charset=charset
    )
    #pymysql로 안의 내용을 통해 접속을 시도하겠습니다. 문서 맨 처음에 선언되어져 있음
    
    startrow = (page-1)*3
    # 1페이지면 startrow가 0
    # 2페이지면 startrow가 3
    # 3페이지면 startrow가 6
    # 스타트로우는 화면에 게시글을 몇 줄까지 보여줄 지 보여줄 변수입니다.
    # 아래에서 추가 설명

    sql = F'select * from freeboard order by idx desc limit {startrow},3'
    # 프리보드에 있는 내용 전부(* = 아스테릭, 뜻은 ALL) order by(순서는~)
    # 내림차순(desc) 최대(limt) startrow 부터 3까지
    # 위에서 startrow는 들어온 page에 따라서 달라지겠죠?
    # page값은 이제 freeboard에서 확인해야 합니다. 
    # 그래서 프리보드 안에 있는 내용을 sql로 담겠다는 뜻입니다.
    cursor = db.cursor()
    #cursor()메소드는 fetchone, fetchall, fetchmany를 사용하게 해준답니다.
    cursor.execute(sql)
    #sql구문을 실행시켜줍니다.
    res = cursor.fetchall()
    #가져온 내용을 res에 담습니다.
    db.close()
    #다른 사람이 사용가능하도록 db연결을 끊어줍니다.
    return res
        
    
    
def insert(title,content,writer):
    db = pymysql.connect(
    host=host,port=port,
    user=user,password=password,
    db=dbname,charset=charset
    )
    sql = f"""
        INSERT INTO freeboard
        (title,content,writer,regdate)
        VALUES
        ('{title}','{content}','{writer}',NOW())   
        """
    cursor= db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()    
    print('insert해야함')
    
def delete(idx):
    db = pymysql.connect(
    host=host,port=port,
    user=user,password=password,
    db=dbname,charset=charset
    )
    sql = f"""DELETE
            FROM freeboard
            WHERE idx= {idx}
    
    """
    print('delete해야함',idx)
    
def update(title,content,writer,idx):
    db = pymysql.connect(
    host=host,port=port,
    user=user,password=password,
    db=dbname,charset=charset
    )
    print('manageboard',idx)
    sql = f"""
        UPDATE freeboard
        SET title = '{title}',
	    content = '{content}',
	    writer = '{writer}'
        WHERE idx = {idx};   
        """
    cursor= db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()    
    print('update 수정해야함')
    