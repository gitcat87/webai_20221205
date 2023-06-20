#include <stdio.h>

int main(){

    int num1;
    int num2;
    int result;
    int i;

    printf("정수입력1: ");
    scanf("%d",&num1);
    printf("정수입력2: ");
    scanf("%d",&num2);
    
    result = num1-num2;
    
    if(num1>num2){
        num1=num1-result;
        num2=num2+result;
    }
     
     while(num1<num2+1){
        while(i<10){
            printf("%d*%d=%d\n",num1,i,num1*i);
            i++;
        }i=1;
        num1++;
        printf("\n");
     }
   
}