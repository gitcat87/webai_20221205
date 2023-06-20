package java230310;

import java.util.Scanner;

class Phone{
	public int hour;
	public int min;
	
	public Phone() {
		this.hour = 0;
		this.min = 0;
	}
	
	// alarm �Լ�  :: "7�ÿ� �˶��� �����մϴ�." ���
	public void alarm() {
		System.out.println("7�ÿ� �˶��� �����մϴ�.");
	}
	
	// clock �Լ� :: "��ٽð��� 9�� 0���Դϴ�." ���
	public void clock() {
		System.out.println("��ٽð��� 9�� 0���Դϴ�.");
	}
	
}

class App extends Phone{
	//��� ����:: hour,min(��� �޾���)
	
	// ������:: hour=h, min=m���� �ʱ�ȭ
	public App(int h, int m) {
		this.hour=h;
		this.min=m;
	}
	
	//alarm�Լ� :: "n�ÿ� �˶��� �����մϴ�." ���
	public void alarm(int n) {
		System.out.println(n+"�ÿ� �˶��� �����մϴ�");
	}
	
	//clock�Լ� :: "��ٽð��� 18�� 0���Դϴ�." ���
	public void clock() {
		System.out.println("��� �ð��� 18�� 0���Դϴ�.");
		
	}
}

public class ex01 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		//�������̵��� �Լ��� clock
		// �����ε��� �Լ��� alarm
		
		Phone p=new Phone();
//		int m=sc.nextInt();
//		int h=sc.nextInt();
//		
		App a = new App(0,0);
		
		// ���� alarm �Լ��� clock �Լ� ����ϱ�
		System.out.println("<Phone ��ü �Լ� ����>");
		p.alarm();
		p.clock();
		System.out.println();
		
		System.out.println("<App ��ü �Լ� ����>");
		a.alarm(155);
		a.clock();
		
	}
}
