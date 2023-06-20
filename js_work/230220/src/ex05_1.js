class Parent{
    constructor() {
        console.log('부모생성자');
    }
    doA() {
        console.log('부모 doA');
    }
}
class Child extends Parent{
    constructor() {
        super(); //부모에 있는 컨스트럭터를 호출
        console.log('자식생성자')
    } //ex05.html로 돌아가서 console.log로 돌아가서 출력
    doA() {
        super.doA();
        console.log('자식 doA');
        //super를 써주면 부모에 있던 doA()도 호출하고
        //자식에 있는 doA()도 호출하게 된다
    }
}


// Parent에 있는 doA()에 있던 함수를
// Child가 상속을 받으면서 Child가 가지고 있던 doA()함수가
// Parent에 있는 doA()함수에 덮어씌워지게 된다.