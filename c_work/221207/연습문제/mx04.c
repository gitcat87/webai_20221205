#include <stdio.h>

int main(){

    int num1, num2, result1, result2;

    printf("input value1 :");
    scanf("%d",&num1);

    printf("input value2 :");
    scanf("%d",&num2);

    result1 = num1/num2;
    result2 = num1%num2;

    printf("value is\n");
    printf("%d\n",result1);
    printf("%d",result2);

    return 0;

}