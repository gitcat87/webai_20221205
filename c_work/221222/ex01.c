#include <stdio.h>

/*
    문제 1
    int arr []=1,2,3,4,5
    ptr 2씩 증가
*/

void main(){

    int arr[] = {1,2,3,4,5};
    int *ptr = arr;

    //출력하는 for 구문

    for(int i=0; i < sizeof(arr)/sizeof(int);i++ ){
        printf("arr[%d] = %d\n",i, arr[i]);
    }
    // 증가시키는 for 구문
    for(int i=0; i < sizeof(arr)/sizeof(int);i++ ){
        ptr[i] = ptr[i]+2;
    }

    for(int i=0; i < sizeof(arr)/sizeof(int);i++ ){
        *(ptr+i) = *(ptr+i) +2; //ptr[1] = ptr[1]+2와 같음
    } //별표(해당되는 주소번지에 가서 값을 읽어라)

    for(int i=4; i>-1;i--){
        *(ptr+i) = *(ptr+i) -1;
    }

    
    
    printf("\n");
    //출력하는 for 구문
    for(int i=0; i < sizeof(arr)/sizeof(int);i++ ){
        printf("arr[%d] = %d\n",i, arr[i]);
    }
}