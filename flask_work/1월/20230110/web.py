from flask \
import Flask, render_template, request, redirect, url_for
import mhpapago
import dbmanager

app = Flask(__name__)

@app.route("/")
def index():
    filename = request.args.get('filename')

    if not filename :
        filename='ex_ko'
    a = [10,20,30,40,50]
    b = [(10,20),('aa','bb'),('한글','되나')]
    res = dbmanager.selectFiles()        
    return render_template("index.html",filename=f"static/{filename}.mp3", a=a, b=b, res=res)

@app.route("/make",methods=['GET','POST'])
def make():
    text = "안녕"
    if request.method =='POST':
        text = request.form['text']
    filename = mhpapago.makePapago(text)
    dbmanager.saveFiles("한국말","영어말",filename)
    return redirect(url_for(f'index',filename=filename))


app.run(debug=True)