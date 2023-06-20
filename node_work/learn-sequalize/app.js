// console.log(__dirname)
// console.log(__filename)

const express = require('express');
const path = require('path');
const morgan = require('morgan');
const nunjucks = require('nunjucks');
const { sequelize } = require('./models');

// const {User} =  require('./models')
// const {commnet} =  require('./models')

require("dotenv").config(); //.env 파일을 가져옴

const app = express();
app.set("port", process.env.port || 3001);
app.set("view engine", "html"); //view엔진은 html로

nunjucks.configure("views",{
    express: app,
    watch:true
})

sequelize.sync({ force: true })
    .then(() => {
        console.log("데이터베이스 생성");
    }).catch((e) => {
    console.log(e)
    })

app.use(morgan("dev"));
app.use(express.static(path.join(__dirname, "public")));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

const indexRouter = require('./routes/index.js');
const usersRouter = require('./routes/users.js');
const commentsRouter = require('./routes/comments.js');

app.use('/', indexRouter);
app.use('/users', usersRouter);
app.use('/comments', commentsRouter);

app.use((req, res, next) => {
    const error = new Error(`${req.method} ${req.url} 라우터가 없습니다.`);
    error.status = 404;
    next(error);
})

app.use((err, req, res, next) => {
    res.locals.message = err.message;
    res.locals.error = process.env.NODE_ENV !== "production" ? err : {};
    res.status(err.status || 500);
    res.render("error");
})



app.listen(app.get('port'), () => {
        console.log(app.get('port'),'번 실행됨')
    })

// console.log(process.env.PORT)