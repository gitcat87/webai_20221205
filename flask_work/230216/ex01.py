from flask import Flask
from flask_cors import CORS, cross_origin
#chrome 브라우저 상에서 발생하는 보안이슈를 해결하는 라이브러리
#flaks_cors // pip install flask_cors

app = Flask(__name__)
#CORS(app)// 모든 페이지에 CORS 오류를 해제한다

@app.route("/")
@cross_origin() #// 해당 페이지에만 CORS오류를 해제한다 해제하고 싶은 페이지에 한줄 추가
def index():
    return "index를 돌려줍니다"


@app.route('/aa')
def aa():
    return 'aa를 돌려줍니다'

app.run(debug=True)