#include <stdio.h>

int main(void){

    int num1[5],i,n;
    for(i=0;i<5;i+=1){
        printf("숫자입력:");
        scanf("%d",&num1[i]);
        printf("입력한숫자는%d\n",num1[i]);        
    }ascending
    
    
    for(n=0;n<5;n++){
        printf("%d",num1[n]);
    }
    return 0;
}