#include <stdio.h>

int main(){

    int i1,i2,i3;
    int total;
    int avg;

    printf("국어 점수 입력 : ");
    scanf("%d",&i1);
    printf("영어 점수 입력 : ");
    scanf("%d",&i2);
    printf("수학 점수 입력 : ");
    scanf("%d",&i3);

    total = i1+i2+i3;
    avg = total/3;
    printf("\n");
    printf("점수 총합 : %d\n",total);
    printf("점수 평균 : %d\n",avg);

    if(avg>=90){
        printf("당신의 학점은 A입니다.");
    }
    else if(avg>=80){
        printf("당신의 학점은 B입니다.");
    }
    else if(avg>=70){
        printf("당신의 학점은 C입니다.");
    }
    else if(avg>=50){
        printf("당신의 학점은 D입니다.");
    }
    else{
        printf("당신의 학점은 F입니다.");
    }

    return 0;
}