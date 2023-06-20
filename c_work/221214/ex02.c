#include <stdio.h>

// 0 ~100사이의 짝수의 합
void ex01(){ 
    int start = 0;
    int total = 0;

    do{
        start = start+2;
        total = total + start;
    }while(start !=100);
    
    printf("total = %d\n\n",total);}

void ex02(){
    int start= 0, end = 0;
    int total= 0;
    printf("시작  정수 입력: \n");
    scanf("%d",&start);
    printf("끝  정수 입력: \n");
    scanf("%d",&end);

    printf("end = %d start = %d",end,start);
    for (int i = start ; i<end+1; i++){
        total = total + i;
    }
    printf("total = %d\n\n",total);
}

void ex03(){
     int input;
   int total = 1;
   printf("구하고 싶은 팩토리얼 정수 입력 : ");
   scanf("%d",&input);

   for(;input>0;input--){
        total =  total*input;
   }
   printf("total = %d",total);
   
}


int main(){
    ex01();
    ex02();
    ex03();

   
   
  
}