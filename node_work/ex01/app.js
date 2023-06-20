// const express = require('express');
// const { sequelize } = require("./models");


class A{
    // 생성자
    constructor(a,b,c,d) {
        // console.log(`a ${a}`);
        // console.log(`b ${b}`);
        // console.log(`c ${c}`);
        // console.log(`d ${d}`);
        this.any = a;
        this.b = b;
        this.c = c;
        this.d = d;        
    }
    doA = () =>{console.log("나옵니다")}
}

const aa = new A();

aa.doA();


