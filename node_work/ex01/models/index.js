'use strict';

const fs = require('fs');
const path = require('path');
const Sequelize = require('sequelize');
const { Model, DataTypes } = require('sequelize');
const process = require('process');
const basename = path.basename(__filename);
const env = process.env.NODE_ENV || 'development';
const config = require(__dirname + '/../config/config.json')[env];
const db = {};


const sequelize = new Sequelize(config.database, config.username, config.password, config);
db.sequelize = sequelize;
db.Sequelize = Sequelize;


const Book = sequelize.define('book',
  {
      title: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    count: {
      type: DataTypes.INTEGER,
    },
})
  
db.Book = Book;
Book.sync({ force: true })
  .then(() => {
  console.log("데이터베이스 연결 성공")
  }).catch((err) => {
    console.log("에러가 발생했습니다." + err);
  })

//방법2
// class Book extends Model {}
// Book.init(
//   {
//     title: {
//       type: DataTypes.STRING,
//       allowNull: false,
//     },
//     cout: {
//       type: DataTypes.INTEGER,
//     },
//   },
//   {
//     sequelize,
//   }
// );

// db.Book = Book;

// Book.sync({ force: true })
// .then(() => {
//   console.log("데이터베이스 연결 성공")
// })
//   .catch((err) => {
//   console.log("에러가 발생했습니다."+err)
// })
// //npx sequelize init
module.exports = db;
