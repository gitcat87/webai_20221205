class Phone {

    public int hour;
    public int min;

    public Phone(int h, int m) {
        this.hour = h;
        this.min = m;
    }

    public void alarm() {
        System.out.println("7시에 알람을 설정합니다");
    }

    public void clock() {
        System.out.println("출근시간은 9시 0분입니다");
    }
}

class app extends Phone {
    
    public app(int h, int m) {
        super(h, m);
    }

    public void alarm(int n) {
        System.out.println(n+"시에 알람을 설정합니다");
    }

    public void clock() {
        System.out.println("퇴근 시간은 18시 0분 입니다.");
    }
    
}

public class ex03 {
    public static void main(String[] args) {
        app em = new app(0, 0);
        em.alarm();
        em.clock();

    }
}
