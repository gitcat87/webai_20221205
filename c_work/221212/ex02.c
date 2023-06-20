#include <stdio.h>

int main(){

    int num1, num2, result;
    int opt;

    while(1){
    printf("어떤 연산을 하시겠습니까 1.(+) 2.(-) 3.(*) 4(/)\n");
    scanf(" %c", &opt);

    printf("opt == %c",opt);
    printf("opt == %d\n",opt);

    printf("첫 번째 수 입력");
    scanf("%d",&num1);

    printf("두 번째 수 입력");
    scanf("%d",&num2);`

    
    if(opt == '+'){
        printf("%d + %d = %d",num1,num2,num1+num2);
    }
    if(opt =='-'){
        printf("%d - %d = %d",num1,num2,num1-num2);
    }
    if(opt =='*'){
        printf("%d * %d = %d",num1,num2,num1*num2);
    }
    if(opt =='/'){
        printf("%d / %d = %d",num1,num2,num1/num2);
    }
    printf("\n");   
    }
}