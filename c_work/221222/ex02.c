#include <stdio.h>

void main(){

    int arr[]  = {1,2,3,4,5,6};

    //포인터를 사용해서 역순으로
    //6 5 4 3 2 1
    int len = sizeof(arr)/sizeof(int);
    int *ptr = NULL;

    for (int start =0,end = len-1; start<len/2; start++,end--){
        printf("start = %d, end =%d\n",start,end);
        int temp = *(arr+end);
        *(arr+end) = *(arr+start);
        *(arr+start) = temp; //*(arr+배열 번호) = arr[배열번호]
    }
        
    for(int i =0; i<len ; i++)
        printf("arr[%d] = %d\n",i,arr[i]);

        
}


