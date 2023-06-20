package java230310;

import java.util.Scanner;

class Phone{
	public int hour;
	public int min;
	
	public Phone() {
		this.hour = 0;
		this.min = 0;
	}
	
	// alarm 함수  :: "7시에 알람을 설정합니다." 출력
	public void alarm() {
		System.out.println("7시에 알람을 설정합니다.");
	}
	
	// clock 함수 :: "출근시간은 9시 0분입니다." 출력
	public void clock() {
		System.out.println("출근시간은 9시 0분입니다.");
	}
	
}

class App extends Phone{
	//멤버 변수:: hour,min(상속 받아짐)
	
	// 생성자:: hour=h, min=m으로 초기화
	public App(int h, int m) {
		this.hour=h;
		this.min=m;
	}
	
	//alarm함수 :: "n시에 알람을 설정합니다." 출력
	public void alarm(int n) {
		System.out.println(n+"시에 알람을 설정합니다");
	}
	
	//clock함수 :: "퇴근시간은 18시 0분입니다." 출력
	public void clock() {
		System.out.println("퇴근 시간은 18시 0분입니다.");
		
	}
}

public class ex01 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		//오버라이딩된 함수는 clock
		// 오버로딩된 함수는 alarm
		
		Phone p=new Phone();
//		int m=sc.nextInt();
//		int h=sc.nextInt();
//		
		App a = new App(0,0);
		
		// 각각 alarm 함수와 clock 함수 사용하기
		System.out.println("<Phone 객체 함수 실행>");
		p.alarm();
		p.clock();
		System.out.println();
		
		System.out.println("<App 객체 함수 실행>");
		a.alarm(155);
		a.clock();
		
	}
}
