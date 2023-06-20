#include <stdio.h>

int main(){
    //포인터 변수

    int num = 5;
    //int *ptr = &num;

    int *ptr; //int형 포인터 변수 ptr 선언

    ptr= &num; //ptr 변수에 num 주소값 투입

    // num의 주소값이 1000이라 가정할때
    // num값음 5, &num값은 1000

    printf("num의 값은 %d\n",num);
    printf("num의 주소값은 %d\n",&num);   

    int arr[10] = {0};
    printf("arr의 주소값은 %d\n",arr);
    //&arr[0] = arr
}