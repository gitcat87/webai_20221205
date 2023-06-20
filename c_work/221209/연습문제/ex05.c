#include <stdio.h>

int main(){

    printf("몇 개의 정수 입력? :");
    int num;
    scanf("%d",&num);

    int cnt = num;
    int total = 0;
    int input =0;

    while( num > 0){
        printf("점수 입력 :");
        scanf("%d",&input);
        total = total + input;
        
        
        num--;
    }
     printf("total = %d\n",total);
     printf("total = %d / %2f\n",total,total/(double)cnt);
    return 0;

}