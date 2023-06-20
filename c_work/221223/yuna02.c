#include <stdio.h>

int sum(int n1, int n2)
{
    printf("덧셈을 수행합니다.\n");
       return n1+n2;  
}

int sub(int n1, int n2)
{
    printf("덧셈을 수행합니다.\n");
       return n1-n2;  
}
int mul(int n1, int n2)
{
    printf("덧셈을 수행합니다.\n");
       return n1*n2;  
}
int div(int n1, int n2)
{
    printf("덧셈을 수행합니다.\n");
       return n1/n2;  
}
int div1(int n1, int n2)
{
    printf("덧셈을 수행합니다.\n");
       return n1%n2;  
}
int main(){
    //사칙연산 함수 구현 (5가지)

    // 1. 2개의 정수 입력받기
    printf("2개의 정수를 입력해주세요.");
    int num1, num2;
    scanf("%d %d",&num1,&num2);
    rewind(stdin);
    
    // 2. 연산자 입력받기
    printf("연산자를 입력해주세요.");
    char ch;
    scanf("%c", &ch);
    

    // 3. 사칙연산 함수 사용

    int result;
    switch(ch){
    case '+': result = sum(num1,num2); break;
        //브레이크를 넣지 않으면 이하 연산을 같은 값으로 출력하게 된다.
    case '-': result = sub(num1,num2); break;               
    case '*': result = mul(num1,num2); break; 
    case '/': result = div(num1,num2); break; 
    case '%': result = div1(num1,num2); break; 
    
    }
    printf("결과값은 %d입니다.\n",result);
}