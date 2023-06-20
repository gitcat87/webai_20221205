package d230308;

//접근 제어자 :: private(클래스 내에서만 접근 가능),public(클래스 외부에서도 접근 가능),protected(상속 개념 포함)

class A{ // 부모클
	
	public int num;	
	protected int a; //A 클래스 내에서 접근 가능, 상속 받은 클래스에서 int a에 접근 가능
}


class B extends A{ //자식클
	public char ch; //B클래스에서만 A클래스의 protected int a 멤버에 접근 가능 -> 상속 받았기 때문 
	
}

class C extends B{
	
	
}
public class ex012 {
	public static void main(String[] args) {
		// 상속 :: "부모의 것을 자식에게 물려준다." 라는 개념에서 파생
		// => 기존의 클래스(부모 클래스)
		// extends 키워드 (extends :: "확장하당")
		
		A a =new A(); //a객체의 멤버 :: num
		B b =new B(); //b객체의 멤버 :: ch, A에서 상속된 num
		
		a.num = 1;
		b.num = 10;
		b.ch='A';
		
		System.out.println("a.num="+a.num);
		System.out.println("b.num="+b.num);
		System.out.println("b.ch="+b.ch);
		
		
	}
}
