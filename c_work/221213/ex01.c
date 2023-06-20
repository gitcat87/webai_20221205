
/*  프로그램 사용자로부터 총 5개의 정수를 입력받아 그 수의 합을
    출력하는 프로그램을 작성해보자
    단 한가지 조건이 있다. 정수는 반드시 1이상이어야 한다. 만약에 1미만의 수가
    입력되는 경우에는 이를 입력하지 않고 재 요구해야 한다.
    그래서 결국 1이상의 정수 5개를 모두 입력받을 수 있도록 완성
   
    문제2
    *
    o *
    o o *
    o o o *
    o o o o *
    참고로 총 5행에 걸쳐서 출력이 이루어지고 행이 더해질때마다 o가 추가됨
    */
#include <stdio.h>

int main(){

    int input = 0, total = 0;
    int num = 5;
    int num1 = 1;
        

    while(num>0){
        printf("%d 번째 정수입력 :",num1);
        scanf("%d",&input);
        
        while(input < 0){
            printf("정수가 0 보다 작습니다. 재입력 하세요 :");
            scanf("%d",&input);
        }
        total = total+input;
        num--; num1++;
        
    }
    printf("입력 받은 수의 합은 %d",total);
    return 0;
}
    
    