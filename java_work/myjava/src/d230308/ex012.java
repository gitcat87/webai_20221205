package d230308;

//���� ������ :: private(Ŭ���� �������� ���� ����),public(Ŭ���� �ܺο����� ���� ����),protected(��� ���� ����)

class A{ // �θ�Ŭ
	
	public int num;	
	protected int a; //A Ŭ���� ������ ���� ����, ��� ���� Ŭ�������� int a�� ���� ����
}


class B extends A{ //�ڽ�Ŭ
	public char ch; //BŬ���������� AŬ������ protected int a ����� ���� ���� -> ��� �޾ұ� ���� 
	
}

class C extends B{
	
	
}
public class ex012 {
	public static void main(String[] args) {
		// ��� :: "�θ��� ���� �ڽĿ��� �����ش�." ��� ���信�� �Ļ�
		// => ������ Ŭ����(�θ� Ŭ����)
		// extends Ű���� (extends :: "Ȯ���ϴ�")
		
		A a =new A(); //a��ü�� ��� :: num
		B b =new B(); //b��ü�� ��� :: ch, A���� ��ӵ� num
		
		a.num = 1;
		b.num = 10;
		b.ch='A';
		
		System.out.println("a.num="+a.num);
		System.out.println("b.num="+b.num);
		System.out.println("b.ch="+b.ch);
		
		
	}
}
