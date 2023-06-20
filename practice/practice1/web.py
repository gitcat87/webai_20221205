from flask import Flask,redirect,render_template,url_for,request


app =  Flask(__name__)


@app.route('/',methods=['POST','GET'])
def index():
    snake= request.args.get('luck')
    print(snake)
    return render_template('/index.html',snake=snake)

@app.route('/index2',methods=['GET','POST'])
def index2():
    luck = request.form['snake']    
    return redirect(url_for('index',luck=luck))

@app.route('/index3')
def index3():
    return render_template('/index3.html')

app.run(debug=True)