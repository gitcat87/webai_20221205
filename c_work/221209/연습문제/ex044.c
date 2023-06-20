#include <stdio.h>

int main(){

    int num, i=9;
    printf("숫자 입력 :\n");
    scanf("%d",&num);

    for(; i>0 ; i--){
        
            printf("%d*%d=%d\n",num,i,num*i);
                
    }
    return 0;
}