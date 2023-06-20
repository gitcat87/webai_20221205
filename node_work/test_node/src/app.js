'use strict'

const express = require('express');
const cors = require('cors');
const mysql = require('mysql2');

const app = express();
app.use(express.json);
app.use(express.urlencoded({ extended: true }));
app.use(cors);

app.get('/', (res, req) => {
    res.send('시작함')
})

app.listen('5000', () => {
    console.log("서버 시작함")
})

console.log("안녕하세요")