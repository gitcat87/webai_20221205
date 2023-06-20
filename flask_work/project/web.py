from flask import Flask,render_template,Blueprint
from components import freeboard
import lotto4

app = Flask(__name__)

app.register_blueprint(freeboard.app)

@app.route("/")
def index():
    return render_template("/index.html")



@app.route("/lotto")
def lotto():
    turn = lotto4.turn[0].text
    number = (lotto4.numbers[0].text,
              lotto4.numbers[1].text,
              lotto4.numbers[2].text,
              lotto4.numbers[3].text,
              lotto4.numbers[4].text,
              lotto4.numbers[5].text)
    potmoney = lotto4.potmoney[0].text
    bonus = lotto4.bonus[0].text
    print(number)
    
    return render_template("/lotto.html",number=number,    
    turn=turn,potmoney=potmoney,bonus=bonus)
    



app.run(debug=True)