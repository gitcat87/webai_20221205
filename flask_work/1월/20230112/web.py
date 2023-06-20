from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route("/")
def index():
    # print(request.args.get('first'))
    # print(request.args.get('second'))
    a = request.args.get("first")
    b = request.args.get("second")
    c =0 
    d=0
    e=0
    f=0
    g=0
    h=0
    
    if a is not None and b is not None:
        c = int(a)+int(b)
        d = int(a)-int(b)
        e = int(int(a)/int(b))
        f = int(a)%int(b)
        g = int(a)**int(b)
        h = int(a)*int(b)
        
    return render_template('index.html',c=c,d=d,e=e,f=f,g=g,h=h)

@app.route("/random")
def random():
    import random
    a = random.randint(1,100)
    return render_template('random.html',a=a)
app.run(debug=True)