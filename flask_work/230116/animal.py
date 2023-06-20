from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('animal.html')

@app.route("/insertform1")
def insertform1():
    return render_template('insertform1.html')

app.run(debug=True)