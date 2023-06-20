package myjava;

class student{
	private String name;
	private int ID;
	private String callDigits;

	//get 메소드 시작
	public String getName() {
		return name;
	}
	public int getID() {
		return ID;
	}
	public String getcallDigits() {
		return callDigits;
	}
	
	//get 메소드 끝
	
	//set 메소드 시작
	public void setName(String nn) {
		name = nn;
	}
	public void setId(int idnum) {
		ID = idnum;
	}
	public void setcallDigits(String digits) {
		callDigits = digits;
	}
	// set 메소드 끝
}

	


	
class person{ //사람클래스
	// 자료형 타입 앞에 private, public
	// private는 다른 클래스 안에서 접근이 안된다.
	private String name; //속성(필드)
	private int age;
	private double height;
	
	// 메소드(함수 = 기능) -> get/set 함수 가장 기본적인 것
	// -> get 함수 :: 특정 속성의 값을 출력하는 함수
	// private String name;에 접근하는 대신 public String getName()의 함수에 접근해서 private String name;의 값을 
	// 가져 올 수 가 있을 것이다.
	public String getName() {
		return name;
	}
	
	// -> set 함수 :: 특정 속성의 값을 수정하는 함수
	public void setName(String n) {
		name=n;
	}
	
}

public class ex04 {
	//클래스 선언

	public static void main(String[] args) {
		// 객체 :: 실생활에서 우리가 볼 수 있는 실체 (클래스로 인해 만들어진 것)
		// 클래스 :: 객체를 만들어내는 틀
		
		// 클래스를 이해하려면
		// 객체 생성하는 방법
		// 변수를 선언할 때 보통 우리는 자료형 타입 그리고 변수이름을 제시한다
		person lee=new person();
		lee.setName("lee");
		person park=new person();
		
		student choi= new student();
		choi.setName("choi");
		choi.setId(25533251);
		choi.setcallDigits("01084953325");
	}
}
