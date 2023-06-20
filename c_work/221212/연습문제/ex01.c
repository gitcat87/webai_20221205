#include <stdio.h>

int main(){

    int num;

    for (int num=1; num<100; num++)
    {
        if(num%7==0||num%9==0)
            printf("7또는 9의 배수 : %d \n",num);        
         
        
        if(num%7==0&&num%9==0)
            printf("7과 9의 배수 : %d\n",num);
    }
    return 0;
}