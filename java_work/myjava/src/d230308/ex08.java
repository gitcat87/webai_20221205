package d230308;


class Phone{
	public int hour;
	public int min;
	
	public Phone(int h, int m) {
		this.hour = h;
		this.min = m;

	}
	
	public void alarm() {
		System.out.println("7�ÿ� �˶��� �����մϴ�");
	}
	
	public void clock() {
		System.out.println("��ٽð��� 9�� 0���Դϴ�.");
	}
}

class app extends Phone{
	
	public app(int h, int m) {
		super(h,m);		
	}
	
	public void alarm(int n) {
		System.out.println(n+"�ÿ� �˶��� �����մϴ�");
	}
	
	public void clock() {
		System.out.println("��ٽð��� 18�� 0���Դϴ�.");
	}

}


public class ex08 {
	public static void main(String[] args) {
	app em = new app(0,0);
	em.alarm(7);
	em.clock();
}
}
