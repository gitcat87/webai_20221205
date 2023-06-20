from flask import Blueprint, render_template, request, redirect
from components.db import freeboardmanage

app = Blueprint('freeboard', __name__, url_prefix='/freeboard')


@app.route('view')
def view():
    idx = int(request.args.get('idx'))
    res = freeboardmanage.selectRow(idx)
    return render_template('freeboard/view.html', res=res)

@app.route("/board")
def board():
    page = request.args.get('page')
    page = 1 if page is None else page
    res = freeboardmanage.select(int(page))
    return render_template('freeboard/board.html', res=res)




