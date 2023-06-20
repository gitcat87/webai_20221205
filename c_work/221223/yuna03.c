#include <stdio.h>

int main(){
    int n = 65;
    printf("숫자로는 %d\n", n); //출력 65
    printf("문자로는 %c\n\n", n); //출력 'A'
    //서식지정을 %d -> %c로 변경했을때 int형 65는 아스키 코드 값65(A)로 변환된다


    char ch = 'a';
    printf("숫자로는 %d\n",ch); 
    printf("문자로는 %c\n\n",ch);

    ch = '0'; //작은 따옴표로 처리하면 문자
    printf("숫자로는 %d\n",ch); 
    printf("문자로는 %c\n\n",ch);

    // 문자형 하나를 입력받고
    // 이를 아스키코드로 변환하여 출력하는 코드 작성
    
    // int aa;
    // printf("입력 :" );
    // scanf("%d",aa)    
    //     if(sizeof(aa)==sizeof(char)){
    //         printf("문자입니다 값은 : %c",aa);}

   
    
    
   
    
}