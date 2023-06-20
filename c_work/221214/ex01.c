/*
 page 161
 문제 2
 0이상 100이하의 정수중에서 짝수의 합을 출력하는 프로그램을 구현하되,
 do~while 문 기반으로 구현해보자
 참고로 덧셈의 결과는 2550이 되어야 한다

 page 167
 for문 활용
 문제1
 프로그램사용자로부터 두개의 정수를 입력 받아서
 두 정수를 포함하여 그사이에 존재하는 정수들의 합을 계산해서 출력하는
 프로그램을 작성해보자 예를 들어서 3과 5가 입력되면 3+4+5로 출력되어야 한다.

 문제2
 다음 수식인 계승을 계산하는 프로그램을 작성하자
 nl = 1*2*3 ... *n
 프로그램사용자로부터 n에 해당하는 정수를 입력받는다
 nl계산해서 출력하자

 page 189[if~else문 활용]

 문제1
 1이상 100미만의 정수 중에서 7의 배수와 9의 배수를 출력하는
 프로그램을 작성하자 단 ! 7의 배수이면서 동시에 9의 배수인 정수는
 한번만 출력되어야 한다.
*/

#include <stdio.h>

int main(){
    int start = 0;
    int total = 0;

    do{
        start = start+2;
        total = total + start;
    }while(start !=100);
    
    printf("total = %d",total);
}