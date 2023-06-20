class Animal {
    public void species() {
        System.out.println("저장된 정보가 없습니다.");

    }

    public void cry() {
        System.out.println("저장된 울음 소리가 없습니다.");
    }
}

class Cat extends Animal {//고양이 클래스
    //오버라이딩 :: 부모 클래스에 있는 멤버(함수)를 "재정의" 하는 행위
    //"덮어 쓰기"의 개념이 포함이 됨

    //멤버 :: species(), cry()
    //다만, species 함수는 매개변수가 없는 상태로도 사용 가능하며
    // 매개변수가 String 하나 있는 경우로도 사용 가능하다.

    public void species(String sp) {
        System.out.println("이 고양이의 종은" + '"'+sp+'"');
    }

    public void cry(String cr) {
        System.out.println("이 고양이는 이렇게 웁니다 "+'"'+cr+'"');
    }
}



public class ex02 {
    public static void main(String[] args) {
        //오버로딩, 오버라이딩
        //오버로딩 :: 반환형 함수이름, 매개변수 구성이 다르면 "오버로딩"
        //  오버로딩의 경우엔, 함수들이 <공존>하여 사용할 수 있다.
        //함수이름, 반환형, 매개변수가 구성이 모두 같으면 "오버라이딩"
        // 오버라이딩의 경우엔, 부모 클래스의 내용을 무시하고
        // 자식클래스의 내용을 우선시함
        Cat c = new Cat();
        c.cry("야오옹");
        c.species("코리안 숏헤어");
    }
}
