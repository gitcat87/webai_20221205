from flask import Flask, render_template, request


app =  Flask(__name__)

@app.route('/')
def base():
    return render_template('/base.html')


@app.route('/index')
def index():
    return render_template('/index.html')

app.run(debug=True)