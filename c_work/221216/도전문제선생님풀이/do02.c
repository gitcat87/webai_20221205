/*
3,5를 입력해도 3,4,5단
5,3을 입력해도 3,4,5단
나오게 만드시오.
*/

#include <stdio.h>

int main(){

    int start = 0, end = 0;
    printf("두개의 수를 입력하세요(띄워쓰기나 엔터키사용가능)");
    scanf("%d %d",&start,&end);

    printf("start  = %d\n",start);
    printf("end  = %d\n",end);

    // 그런데 이렇게 해놓으면 마지막엔 두개의 값이 같아지기 때문에
    // temp라는 임시 변수를 만들어서 start의 값을 저장해놓자

    if (end < star);

    int temp = start;
    start = end;
    end = temp;
    
    // start * 1 =... *2 *3 *4 *5 <end+1
    for ( ; start < end+1 ; start++ ){
        for(int i = 1 ; i < 10; i++ ){
            printf("%d*%d=%d\n",start,i,start*i);
        }
    }
    printf("\n");
}