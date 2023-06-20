from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)


@app.route('/')
def index():
    return """<h1>index<h1>
                <a href='insertform'>insertform</a>
                <a href='insert'>insert</a>
                <a href='select'>select</a>
            """


@app.route('/insertform')
def insertform():
    return render_template('insertform.html')


@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'GET':
        a = request.args.get('a')
        b = request.args.get('b')
        c = request.args.get('c')
    elif request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        c = request.form['c']

    a = 100 if a is None or a is "" else a
    b = 100 if b is None or b is "" else b
    c = 100 if c is None or c is "" else c
    db = pymysql.connect(host="127.0.0.1", port=3306,
                         user="root", passwd="root123",
                         db="DHchoi", charset="utf8")
    cursor = db.cursor()
    sql = f"""insert into
            TB_A
            values
            ({a},{b},'{c}')
            """
    cursor.execute(sql)
    db.commit()
    db.close()
    return "insert"


@app.route('/select')
def select():
    db = pymysql.connect(host="127.0.0.1", port=3306,
                         user="root", passwd="root123",
                         db="DHchoi", charset="utf8")
    cursor = db.cursor()
    sql = """select * from TB_A """
    cursor.execute(sql)
    res = cursor.fetchall()
    db.close()
    return str(res)


app.run(debug=True)
