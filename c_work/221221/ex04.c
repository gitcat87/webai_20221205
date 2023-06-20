#include <stdio.h>

void main(){

    int arr[3][4] = { //가로요소는 채워야 한다. 세로요소는 비워도 괜찮음
        {1,2,3}, //배열 가로 4, 세로 3
        {4,5},  // [1,2,3,4]
                // [4,5,0,0]
        {6,7,8},// [6,7,8,0]

    };

    printf("sizeof(arr) %d\n",sizeof(arr));
    printf("sizeof(arr[0]) %d\n",sizeof(arr[0]));
    printf("sizeof(arr[1]) %d\n",sizeof(arr[1]));
    printf("sizeof(arr[2]) %d\n",sizeof(arr[2]));

    for (int x = 0; x < 3; x++) //sizeof(arr)/sizeof(arr[0]);
                                //sizeof함수를 이용하여 세로 값을 구하는 방법
                                //sizeof함수로 2차원 배열 전체의 값을 구하고
                                //가로의 값으로 전체를 나누면 세로의 값이 나온다
        {
            for (int y = 0; y < 4; y++){
                printf("arr[%d][%d] = %d",x,y,arr[x][y]);
            }
            printf("\n");
        }

}