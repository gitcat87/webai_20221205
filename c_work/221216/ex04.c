#include <stdio.h>

int main(){

    int arr[] = {10,20,30};

    printf("arr = %d\n", arr);
    printf("arr+1 = %d\n", arr+1);
    printf("arr+2 = %d\n", arr+2);
    printf("\n");
    int *p = &arr[0];
    printf("p = %d\n", p);
    printf("p+1 = %d\n", p+1);
    printf("p+2 = %d\n", p+2);
    
}