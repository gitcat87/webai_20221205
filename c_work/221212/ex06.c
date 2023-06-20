#include <stdio.h>

int main(){

    printf("숫자 입력: ");
    int num;
    scanf("%d",&num);

    switch (num)
    {
    case 10:
            printf("num 은 10 입니다");
        break;

    case 20:
            printf("num 은 20 입니다");
        break;

    case 30:
            printf("num 은 30 입니다");
        break;
    default:
            printf("default...");
        break;
    }
    
}