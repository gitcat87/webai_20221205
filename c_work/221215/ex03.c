#include <stdio.h>

int main(){

    int arr[]={1,2,3,4,5,2,6,4,6,3,4,2,3,5,6,2};

    printf("sizeof = %d", sizeof(arr));
    int len = sizeof(arr)/sizeof(int); //size(int)<-- 4바이트로 나눈다
    printf("len = %d",len);

    for (int i=0; i<len;i++){
        printf("arr[%d] = %d\n",i,arr[i]);
    }
}