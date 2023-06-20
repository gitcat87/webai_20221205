#include <stdio.h>

int main(){

 
    int a,b,c;
    printf("숫자 입력1 :");
    scanf("%d",&a);
    printf("숫자 입력2 :");
    scanf("%d",&b);
    printf("숫자 입력3 :");
    scanf("%d",&c);

    if(a < b && a < c){        
            printf("%d은 최소숫자입니다.",a);

        }else if(b < a && b < c){
            printf("%d은 최소숫자입니다.",b);
        }
        else{
        printf("%d은 최소숫자입니다.",c);
    }
    printf("\n");
    if(a > b && a > c){        
            printf("%d은 최대숫자입니다.",a);

        }else if(b > a && b > c){
            printf("%d은 최대숫자입니다.",b);
        }
        else{
        printf("%d은 최대숫자입니다.",c);
    }   

}