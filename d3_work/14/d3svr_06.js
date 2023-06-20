var db_host = "localhost";
var db_port = 1521;
var db_name = "xe";
var db_id = "kb";
var db_pwd = "kb602";

var port = 3000;

const _express = require("express");
const _app = _express();

var _cors = require("cors");
_app.use(_cors());

//오라클호출
const oracledb = require("oracledb");
const moment = require("moment-timezone");

//기본 루트 호출--
_app.get("/", function (req, res) {
  res.send("HelloWorld");
});

//Get Query 방식
//http://localhost:3000/user/info?name=kim&age=18&birthday=12/25
_app.get("/user/:info", function (req, res) {
  const _q = req.query;
  console.log(_q);
  _name = _q.name;
  _age = Number(_q.age);
  _birthday = _q.birthday;
  if (_age < 20) {
    res.send(`${_name}은 술담배를 구매할수 없습니다.`);
  } else {
    res.send(`${_name}님은 주류구매가 가능하십니다.`);
  }
});
//------------------------------------
//Get 방식으로  D3요청사항 처리하기
//http://localhost:3000/d3/info?work=01&year=2023&month=12
_app.get("/d3/:info", function (req, res) {
  const _q = req.query;
  console.log(_q);
  if (_q.work == "01") {
    //막대그래프요청
      var ThisYear = Number(_q.year);
      var ThisMonth = Number(_q.month);
      var NextYear = ThisYear;
      var NextMonth = ThisMonth + 1;
      if (NextMonth > 12) {
          NextYear = ThisYear + 1;
          NextMonth = 1;

      }
    var _query = `
    SELECT TO_CHAR(all_dates.OUT_DATE, 'YYYY-MM-DD') AS DATE_FORMAT, NVL(SUM(CDH_OUT.OUT_PRICE), 0) AS DAILY_SALES
    FROM (
      SELECT TO_DATE('${ThisYear}-${ThisMonth}-01') + LEVEL - 1 AS OUT_DATE
      FROM dual
      CONNECT BY LEVEL < TO_DATE('${NextYear}-${NextMonth}-01','YYYY-MM-DD') - TO_DATE('${ThisYear}-${ThisMonth}-01','YYYY-MM-DD') + 1
    ) all_dates
    LEFT JOIN KB.CDH_OUT ON all_dates.OUT_DATE = CDH_OUT.OUT_DATE
    GROUP BY all_dates.OUT_DATE
    ORDER BY all_dates.OUT_DATE      
    `;
    console.log(_query);
    ExcuteOracle(db_host, db_port, db_name, db_id, db_pwd, res, _query);
  } else if (_q.work == "02") {
    //원그래프요청사항
            var ThisYear = Number(_q.year);
            var ThisMonth = Number(_q.month);
            var NextYear = ThisYear;
            var NextMonth = ThisMonth + 1;
            if (NextMonth > 12) {
              NextYear = ThisYear + 1;
              NextMonth = 1;
            }
            var _query = `
        SELECT TO_CHAR(OUT_DATE, 'DAY') AS DAY_OF_WEEK, SUM(OUT_PRICE) AS TOTAL_SALE_PRICE
        FROM KB.CDH_OUT
        WHERE OUT_DATE >= TO_DATE('${_q.begin}', 'YYYY-MM-DD')
        AND OUT_DATE <= TO_DATE('${_q.end}', 'YYYY-MM-DD')
        GROUP BY TO_CHAR(OUT_DATE, 'DAY')     
    `;
            console.log(_query);
            ExcuteOracle2(db_host, db_port, db_name, db_id, db_pwd, res, _query);
  } else if (_q.work == "03") {
    //꺽은선 그래프 요청 사항
                  var _query = `
    SELECT TO_CHAR(OUT_DATE, 'MM') AS MONTH,
       SUM(OUT_PRICE) AS TOTAL_SALES
    FROM KB.CDH_OUT
    WHERE EXTRACT(YEAR FROM OUT_DATE) = ${_q.year}
    GROUP BY TO_CHAR(OUT_DATE, 'MM') 
    `;
                  console.log(_query);
                  ExcuteOracle2(
                    db_host,
                    db_port,
                    db_name,
                    db_id,
                    db_pwd,
                    res,
                    _query
                  );
  }
});

//------------------------------------
_app.listen(port, () => {
  console.log(`D3SVR listening on ${port} port`);
});

//오라클 처리함수 ---
function ExcuteOracle(host, port, database, id, pwd, res, query) {
  oracledb.getConnection(
    {
      user: id,
      password: pwd,
      connectString: `${host}:${port}/${database}`,
    },
    (err, connection) => {
      if (err) {
        console.error(err.message);
        return res
          .status(500)
          .json({ error: "데이터베이스 연결에 실패했습니다." });
      }
      console.log("데이터베이스에 연결되었습니다.");
      connection.execute(
        query,
        {},
        { outFormat: oracledb.OUT_FORMAT_OBJECT },
        (err, result) => {
          if (err) {
            console.error(err.message);
            doRelease(connection); //디비접속끊기
            return res.status(500).json({ error: "쿼리실행중 오류발생" });
          }
          //쿼리 성공시

          // 결과 행을 순회하면서 날짜 형식을 변경합니다.
          const formattedRows = result.rows.map(row => ({
            DATE_FORMAT: moment(row.DATE_FORMAT).format("YYYY-MM-DD"),
            DAILY_SALES: row.DAILY_SALES,
          }));

          res.json(formattedRows);
          console.log(formattedRows);
          //res.json(result.rows);
          //console.log(result.rows);
          doRelease(connection); //DB접속 끊기
        }
      );
    }
  );
}
//ExecuteOracle2
function ExcuteOracle2(host, port, database, id, pwd, res, query) {
  oracledb.getConnection(
    {
      user: id,
      password: pwd,
      connectString: `${host}:${port}/${database}`,
    },
    (err, connection) => {
      if (err) {
        console.error(err.message);
        return res
          .status(500)
          .json({ error: "데이터베이스 연결에 실패했습니다." });
      }
      console.log("데이터베이스에 연결되었습니다.");
      connection.execute(
        query,
        {},
        { outFormat: oracledb.OUT_FORMAT_OBJECT },
        (err, result) => {
          if (err) {
            console.error(err.message);
            doRelease(connection); //디비접속끊기
            return res.status(500).json({ error: "쿼리실행중 오류발생" });
          }
          //쿼리 성공시

          // 결과 행을 순회하면서 날짜 형식을 변경합니다. 
          res.json(result.rows);
          console.log(result.rows);
          doRelease(connection); //DB접속 끊기
        }
      );
    }
  );
}


//디비접속끊기 함수
function doRelease(connection) {
  connection.close(err => {
    if (err) {
      console.error(err.message);
    }
    console.log("데이터베이스 연결이 닫혔습니다.");
  });
}
