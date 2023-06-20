#include <stdio.h>

int main(){

    int num1 = 10 , num2 =20;

    int *ptr1 = &num1;
    int *ptr2;
    ptr2 =&num2;

    *ptr1 +=10; //별표를 만나게 되면 해당되는 주소의 값에 가서 우변의 값을 더함
    *ptr2 -=10;
    
    printf("*ptr1 = %d\n", &num1);
    printf("*ptr2 = %d\n", &num2);

    printf("*ptr1 = %d\n", *ptr1);
    printf("*ptr2 = %d\n", ptr2);


    ptr1 = &num2;
    ptr2 = &num1;

    printf("*ptr1 = %d\n", *ptr1);
    printf("*ptr2 = %d\n", *ptr2);
}