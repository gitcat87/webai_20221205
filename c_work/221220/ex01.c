#include <stdio.h>

void main(){
    int max = 0;
    int min = 0;
    int total = 0;

    int arr[5];

    for(int i = 0; i<5; i++){

        printf("정수 입력");
        scanf("%d",&arr[i]);   //arr[?번째]에 입력
        total += arr[i]; //arr[?번째]값
           

        //최소 최대값 구하기는 하나의 공간을 마련해두고
        //그 공간안에 입력 받은 값을 넣는다
        //넣은 값과 다음 값을 비교해서 크면 넣고 아니면 그대로 둔다
        //최소값도 마찬가지로 진행
    }

    for(int i=0; i<5; i++){
        if(max < arr[i])
            max = arr[i];
    }//i(5개의 입력받은 수가 5보다 작을때 동작을 반복)
    //맥스 값이 입력받은 수 보다 클 때
    //맥스 값을 교체

    min = arr[0];
    for(int i=0; i<5; i++){
        if(min > arr[i])
        min = arr[i];
    }
    //위의 맥스 값과 반대
    printf("\n");
    for(int i =0;i<5;i++){
        printf("arr[%d] = %d\n",i,arr[i]);
    }
    printf("\n");
    printf("total = %d\n",total);
    printf("min = %d\n",min);
    printf("max = %d\n",max);
}