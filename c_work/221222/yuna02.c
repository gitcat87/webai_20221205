#include <stdio.h>

int main(){

//1차원 배열 :: 점수들을 입력받고 최대값, 최소값 추려내기

//1. 배열선언(5개)
// 아직 값을 별도로 넣지 않아서 -> 쓰레기 값이 들어있음

int score[5];

//2. 입력 받기

for(int i=0; i<5;i++){
    printf("점수를 입력해주세요.:\n");
    scanf("%d",&score[i]); // 0~4번까지 입력
}

//3. 최대값, 최소값 추려내기
    int max=0, min=100;
    for(int i=0;i<5;i++){
        if(max<score[i]){max = score[i];}
        if(min>score[i]){min = score[i];}
    }

//4. 정답 출력하기
    printf("최대는 %d, 최소는 %d\n",max,min);
}