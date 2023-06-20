from flask import Blueprint, render_template, redirect, url_for, request


app = Blueprint('line',__name__, url_prefix='/lineOne')

@app.route('/seolhwa')
def seolwha():
    return render_template('lineOne/seolhwa.html')