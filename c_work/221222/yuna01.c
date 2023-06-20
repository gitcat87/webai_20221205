#include <stdio.h>

// 2중 반복문, 배열, 포인터
int main(){
    //2중 반복문 -> "별 찍기"

    //1. 입력값 받기
    int n;
    scanf("%d",&n);
    //n을 5줄로 받았을때
    //2. 이중 반복문 설계
    for (int i =1;i<=n;i++){
        for(int j = 1; j<=i;j++){
            printf("*");
        }
        printf("\n");  
    }
           

}
