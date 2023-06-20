#include <stdio.h>

int main(){

    int num1 = 0;
    
    printf("숫자 입력 : ");
    scanf("%d",&num1);
    int num2 = num1+num1;

    while(num1<num2){

        printf("hello world!");
        printf("\n");
        num1++;
        }
    return 0;
}
