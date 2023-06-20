#include <stdio.h>

int main(){

    int num1, result;

    printf("값을 입력하세요 : ");
    scanf("%d",&num1);

    result = num1*num1;

    printf("결과는\n");
    printf("%d*%d=%d\n",num1,num1,result);
    printf("입니다.");

    return 0;
}
