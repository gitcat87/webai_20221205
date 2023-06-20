#include <stdio.h>

int main(){

    int num = 10;
    int *ptr1 = &num;
    //int *ptr1;
    //ptr1 = &num;
    int *ptr2 = ptr1;

    printf("ptr1 = %d \n", ptr1);
    printf("ptr2 = %d \n", ptr2);
    (*ptr1)++; //ptr1의 주소값에 가서 포인터변수를 읽어라
    (*ptr2)++;
    printf("%d \n", num);
}