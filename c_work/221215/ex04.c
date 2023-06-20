#include <stdio.h>

int main(){

    char str[] = "Good Morning!";

    printf("sizeof(str) = %d \n ",sizeof(str));

    str[12]= '?';
    //%s 는 \0 널 문자가 있는데 까지 출력을 한다 
    printf("str[13] = %c\n",str[13]);
    printf("str[13] = %d",str[13]);
}