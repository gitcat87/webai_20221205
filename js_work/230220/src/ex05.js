class Square{
    static count=0
    constructor(legnth) {
        this.legnth = legnth;
        Square.count = Square.count + 1;      
        console.log(`생성자에서 Square.count =${Square.count}`)
    }
    print() {
        console.log(Square.count);
    }
}