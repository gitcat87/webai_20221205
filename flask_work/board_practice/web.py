from flask import Flask, render_template, request
from components.db import freeboardmanage

app = Flask(__name__)


@app.route("/view")
def view():
    idx = int(request.args.get('idx'))
    res = freeboardmanage.selectRow(idx)
    return render_template('/view.html', res=res)



@app.route("/")
def index():
    page = request.args.get('page')
    page = 1 if page is None else page
    res = freeboardmanage.select(int(page))
    return render_template('index.html',res=res)




app.run(debug=True)