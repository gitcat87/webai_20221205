package myjava;

class student{
	private String name;
	private int ID;
	private String callDigits;

	//get �޼ҵ� ����
	public String getName() {
		return name;
	}
	public int getID() {
		return ID;
	}
	public String getcallDigits() {
		return callDigits;
	}
	
	//get �޼ҵ� ��
	
	//set �޼ҵ� ����
	public void setName(String nn) {
		name = nn;
	}
	public void setId(int idnum) {
		ID = idnum;
	}
	public void setcallDigits(String digits) {
		callDigits = digits;
	}
	// set �޼ҵ� ��
}

	


	
class person{ //���Ŭ����
	// �ڷ��� Ÿ�� �տ� private, public
	// private�� �ٸ� Ŭ���� �ȿ��� ������ �ȵȴ�.
	private String name; //�Ӽ�(�ʵ�)
	private int age;
	private double height;
	
	// �޼ҵ�(�Լ� = ���) -> get/set �Լ� ���� �⺻���� ��
	// -> get �Լ� :: Ư�� �Ӽ��� ���� ����ϴ� �Լ�
	// private String name;�� �����ϴ� ��� public String getName()�� �Լ��� �����ؼ� private String name;�� ���� 
	// ���� �� �� �� ���� ���̴�.
	public String getName() {
		return name;
	}
	
	// -> set �Լ� :: Ư�� �Ӽ��� ���� �����ϴ� �Լ�
	public void setName(String n) {
		name=n;
	}
	
}

public class ex04 {
	//Ŭ���� ����

	public static void main(String[] args) {
		// ��ü :: �ǻ�Ȱ���� �츮�� �� �� �ִ� ��ü (Ŭ������ ���� ������� ��)
		// Ŭ���� :: ��ü�� ������ Ʋ
		
		// Ŭ������ �����Ϸ���
		// ��ü �����ϴ� ���
		// ������ ������ �� ���� �츮�� �ڷ��� Ÿ�� �׸��� �����̸��� �����Ѵ�
		person lee=new person();
		lee.setName("lee");
		person park=new person();
		
		student choi= new student();
		choi.setName("choi");
		choi.setId(25533251);
		choi.setcallDigits("01084953325");
	}
}
