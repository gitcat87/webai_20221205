//이번에는 객체를 반환해보자
//main.js 에서는 함수를 반환 했다.
const a = require('../com/a1.js');
const b = require('../com/b1.js');

console.log(a);
console.log(b);

console.log(`a ${a}`);
console.log(`b ${b}`);

console.log(`JSON stringfy(a) ${JSON.stringify(a)}`); 
console.log(`JSON stringfy(b) ${JSON.stringify(b)}`);


console.log('main.js');