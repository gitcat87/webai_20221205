// console.log('b.js');

class Person {
  a = 20;
  b;
  constructor(a, b) {
    this.a = a;
    this.b = b;
  }
  doA = () => {
    console.log(`this.a ${this.a}`);
  };
}
const person1 = new Person(30, "bbb");
const person2 = new Person(40);

// console.log(person1)
// console.log(person2)

// const aa = {};
// aa.person1 = person1;
// aa.person2 = person2;

// module.exports = aa;

// module.exports = {person1,person2};

const aa = {
  person1,
  person2,
};

module.exports = aa;







// //사람 클래스

// console.log('b.js');

// class Person{
//     a = 20;
//     constructor(a) {
//         this.a = a; //파라미터 값을 받아서 person이라는 클래스의 a의 값을 변경해주려고 한다 this를 써서 c#에서 제공하는 문법
//     }
//     doA = () => { console.log(`a ${this.a}`) };

// }

// const person1 = new Person(30);
// const person2 = new Person(40);

// module.exports = person1;

// //컨스트럭트라는 것은 new person을 했을때 컨스트럭트 안의 내용이 불러오게 되어있다.
// // 원래믄 a의 값이 20이었는데 new person을 하면서 a의 값은 30으로 바뀌게 된다
