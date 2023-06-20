#include <stdio.h>

int main(){

    int arr1[3][2]={0};
    int arr2[2][3]={0};

    printf("======== arr1 주소값 ========\n");
    printf("arr1 = %d\n", arr1);
    printf("arr1+1 = %d\n", arr1+1);
    printf("arr1+2 = %d\n\n", arr1+2);

    printf("======== arr2 주소값 ========\n");
    printf("arr2 = %d\n", arr2);
    printf("arr2+1 = %d\n", arr2+1);
  

    printf("======== arr1 값 ========\n");
    printf("**arr1 = %d\n", **arr1);
    printf("**(arr1+1) = %d\n", **(arr1+1));
    printf("**(arr1+2) = %d\n\n", **(arr1+2));

    printf("======== arr2 값 ========\n");
    printf("**arr2 = %d\n", **arr2);
    printf("**(arr2+1) = %d\n", **(arr2+1));
    

}