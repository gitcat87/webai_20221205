class Book {
    private String name;
    private String writer;

    public Book(String n, String w) { //Book클래스의 생성자
        this.name = n;
        this.writer = w;
        System.out.println("책 이름 :" + this.name);
        System.out.println("저자이름:"+this.writer);
    }
}

class Pbook extends Book {
    //멤버: name, writer
    private int paper;

    public Pbook(String n, String w, int p) {
        super(n, w);
        this.paper = p;
        System.out.println("종이 사이즈 :"+this.paper);
    }
    //"자식 클래스의 객체 생성할 때, 반드시 부모 생성자부터 실행을 한다."
    //super(n,w):: 부모클래스의 생성자를 싱행

}

class Ebook extends Pbook{
    //멤버: name, writer, os, paper
    private String os;

    public Ebook(String n, String w, int p, String o) {
        super(n, w, p);
        this.os = o;
        System.out.println("호환 :Os"+this.os);
    }
}


public class ex01 {
    public static void main(String[] args) {
        Pbook p1 = new Pbook("Java", "Lee", 1500);
        System.out.println();
        Ebook e1 = new Ebook("React", "Park", 2000, "IceSand");
    }
}
