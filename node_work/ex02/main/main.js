const a = require('../com/a.js');
const b = require('../com/b.js');

console.log(`a ${a}`); //1. 문자열로 출력한 것이 아니라 객체로 출력해서 a [object object] 나오고
console.log(`b ${b}`);

a(); //얘는 함수 실행
b();

const c = () => { console.log('c함수') };
console.log(c);
console.log(`c ${c}`);
c();

// console.log(`a ${JSON.stringify(a)}`); //2. 클래스를 문자열로 출력해 달라.. 근데 내용이 없기 때문에 {} 빈 객체로 나온다.
// console.log(`b ${JSON.stringify(b)}`);


console.log('main.js');