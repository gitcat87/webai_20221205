#include <stdio.h>

int main(){

    int num1, num2, num3, result;

    printf("value 1 :");
    scanf("%d",&num1);

    printf("value 2 :");
    scanf("%d",&num2);

    printf("value 3 :");
    scanf("%d",&num3);

    result = (num1-num2)*(num2+num3)*(num3%num1);
    printf("%d",result);

    return 0;
}