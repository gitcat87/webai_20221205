class DD{
    static doA(aa) {
        console.log(aa);
        aa.person1.a = 50;
    }
    static doB(aa) {
        aa.person2.a = 80;
    }
}

module.exports = DD;