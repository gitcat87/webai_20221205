from flask import Flask,render_template,request,Blueprint,redirect,url_for
import freeboard, fileboard


app = Flask(__name__)

app.register_blueprint(freeboard.app)
app.register_blueprint(fileboard.app)

@app.route("/")
def index():
    return render_template('index.html')

app.run(debug=True,port=5000,host='0.0.0.0')