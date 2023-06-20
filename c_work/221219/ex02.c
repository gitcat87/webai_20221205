#include <stdio.h>

int main(){
    int arr[3] = {11,22,33};

    int *ptr;
    ptr =&arr[0];

    printf("주소값 ptr %d\n",ptr);
    printf("주소값 ptr+1 %d\n", ptr+1);
    printf("주소값 ptr+2 %d\n", ptr+2);
    printf("\n");
    printf("값 *ptr %d\n",*ptr);
    printf("값 *(ptr+1) %d\n",*(ptr+1));
    printf("값 *(ptr+2) %d\n",*(ptr+2));
    printf("\n");
    printf("값 ptr %d\n",ptr[0]);
    printf("값 ptr1 %d\n",ptr[1]);
    printf("값 ptr2 %d\n",ptr[2]);
}