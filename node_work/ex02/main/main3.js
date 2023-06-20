const c = require('../com/c.js');

c.Myc.doA();
c.myc.doB();



//static은 선언하는 순간 메모리 상에 올라가 있다.
//doB는 함수 선언만 했지 메모리 상에 올라가 있지 않기 때문에 값을 담아서 메모리에 올려주지 않고 호출하게 되면 오류가 난다
//static은 override가 가능하다.
//보통 static함수는 static함수끼리만 사용하고 변경을 하지 않는다.