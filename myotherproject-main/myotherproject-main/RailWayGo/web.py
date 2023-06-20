from flask import Flask, render_template, redirect, url_for, Blueprint
from components import line



app =  Flask(__name__)

app.register_blueprint(line.app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/line")
def line():
    return render_template('RAIL/line.html')


app.run(debug=True)