#include <stdio.h>

int main(){

  int num = 10;
  int dan = 0;  

    printf("입력 :");
    scanf("%d",&dan);

    while(0<num){

        num--;
        printf("%d* %d =%d\n", dan,num,dan*num);
        
    }
    return 0;
}