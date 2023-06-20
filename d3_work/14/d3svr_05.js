/*
npm init
npm i express
npm i cors
npm i oracledb
*/

var db_host = '192.168.0.80';//'localhost';//'localhost';
var db_port = 1521;
var db_name = 'xe';
var db_id   = 'kb';
var db_pwd  = 'kb602';

var port =3000;
const _express = require('express')
const _app = _express();

//주소창에 값을 입력만 받고  fetch등 자바스크립트로 요청했을때는
//에러가 발생하는데
//자바스크립트 요청에도 응답하게 해주는 코드
var _cors = require('cors')  
_app.use(_cors())

//오라클 설정
const oracledb = require('oracledb');


_app.get('/', function(req,res){
  res.send('Hello World')
});

_app.get('/dog', function(req,res){
  res.json({'sound':'멍멍'})
})

_app.get('/cat', function(req, res){
  res.json({'sound':'야옹'})
})

//파람(param)사용하는 방법
_app.get('/animal/:id',function(req,res){
  const q = req.params;
  console.log(q);
  if(q.id == 'pig') {
    res.json({'id':q.id,'sound':'꿀꿀'})

  } else if(q.id == 'duck') {
    res.json({'id':q.id,'sound':'꽥꽥'})

  } else if(q.id == 'cat') {
    res.json({'id':q.id,'sound':'야용'})

  } else {
    res.json({'id':q.id,'sound':'모름'})
  }
})

//쿼리를 사용하는 방법
//http://localhost:3000/user/query?name=kim&age=100

_app.get('/user/:query', function(req,res){
  const _q = req.query;
  _name = _q.name;
  _age  = _q.age;
  _birthday = _q.birthday;

  res.json({'이름':_name,'나이':_age,'생일':_birthday})
})

//쿼리를 사용해서 오라클 처리하기
_app.get('/d3/:category', function(req,res){
  const _q = req.query;
  if(_q.work == '00'){
    var _query = 'SELECT ctg_ucode, ctg_depth, ctg_name, ctg_ucode_super,ctg_index FROM kb_category';
    console.log(_query);
    ExcuteOracle(db_host,db_port,db_name, db_id, db_pwd, res, _query);
  } else if(_q.work == '01'){

    var _query = `    
      SELECT TO_CHAR(RNT_RENT_DATE, 'DAY') AS RENTAL_DAY, COUNT(rnt_ucode) AS RENTAL_COUNT FROM KB_RENT
      WHERE RNT_RENT_DATE >= DATE '${_q.begin}' AND RNT_RENT_DATE <= DATE '${_q.end}'
      GROUP BY TO_CHAR(RNT_RENT_DATE, 'DAY'), TO_CHAR(RNT_RENT_DATE, 'D')
      ORDER BY TO_CHAR(RNT_RENT_DATE, 'D'), TO_CHAR(RNT_RENT_DATE, 'DAY')
    `;
    console.log(_query);
    ExcuteOracle(db_host,db_port,db_name, db_id, db_pwd, res, _query);
  } else if(_q.work == '02'){
    var ThisYear = Number(_q.YEAR)
    var ThisMonth = Number(_q.MONTH)
    var NextYear = ThisYear;
    var NextMonth = ThisMonth+1;
    if(NextMonth>12) {
      NextMonth  = 1;
      NextYear   = NextYear+1;
    }

    console.log("-----------------")
    console.log(`${ThisYear}  , ${ThisMonth}  , ${NextYear}  , ${NextMonth}  `)
    var _query = `
    SELECT
        TO_CHAR(GEN_DATE, 'YYYY-MM-DD') AS CLS_DATE,
        COUNT(CLS_DATE) AS RECORD_COUNT
    FROM
        (SELECT TO_DATE('${ThisYear}-${ThisMonth}-01', 'YYYY-MM-DD') + LEVEL - 1 AS GEN_DATE
        FROM DUAL
        CONNECT BY LEVEL < (TO_DATE('${NextYear}-${NextMonth}-01', 'YYYY-MM-DD') - TO_DATE('${ThisYear}-${ThisMonth}-01', 'YYYY-MM-DD')) + 1
        ) ALL_DATES
    LEFT JOIN
        KB.PGH_CLASS ON TRUNC(GEN_DATE) = TRUNC(CLS_DATE)
    WHERE
        GEN_DATE BETWEEN TO_DATE('${ThisYear}-${ThisMonth}-01', 'YYYY-MM-DD') AND TO_DATE('${NextYear}-${NextMonth}-01', 'YYYY-MM-DD')
    GROUP BY
        TO_CHAR(GEN_DATE, 'YYYY-MM-DD')
    ORDER BY
        TO_CHAR(GEN_DATE, 'YYYY-MM-DD')
    `;
    console.log(_query);
    ExcuteOracle(db_host,db_port,db_name, db_id, db_pwd, res, _query);

  }  


});

_app.listen(port,()=>{
  console.log(`D3SVR listening on ${port} port`)
})


///오라클 접속해서 데이터를 얻어온뒤  json형식으로 반환 하는 함수 ----
function ExcuteOracle(host, port, database, id, pwd, res, query){

  oracledb.getConnection(
    {
      user: id,
      password: pwd,
      connectString: `${host}:${port}/${database}`
    },(err, connection)=>{
      if(err){
        console.error(err.messege);
        return res.status(500).json({error:'데이터베이스 연결에 실패했습니다.'});
      }
      console.log('데이터베이스에 연결되었습니다.');
      connection.execute(
        query, {},
        {outFormat: oracledb.OUT_FORMAT_OBJECT },
        (err, result)=>{
          if(err){
            console.error(err.message);
            doRelease(connection);//접속끊기
            return res.status(500).json({error:'쿼리를 실행중 오류가 발생했습니다.'})
          }
          //쿼리실행에 성공하면
          res.json(result.rows);
          console.log(result.rows);
          doRelease(connection);
        }
      );

    }
  ); 
} // END function : ExcuteOracle ----------------------

function doRelease(connection){
  connection.close((err)=>{
    if(err){
      console.error(err.message);
    }
    console.log('데이터베이스 연결이 닫혔습니다.');
  })
}
