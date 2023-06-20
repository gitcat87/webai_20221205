#include <stdio.h>

int main(){

    int num1, num2, result;

    printf("첫 번째 값을 입력하세요:");
    scanf("%d",&num1);

    printf("두 번째 값을 입력하세요:");
    scanf("%d",&num2);

    result = num1 + num2;

    printf("결과는...");
    printf("\n");
    printf("%d+%d=%d\n", num1, num2, result);
    printf("입니다.");

    return 0;
}