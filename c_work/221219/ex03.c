#include <stdio.h>

void whoareyou(char *test){
    printf("==============whoareyou start================\\n");
    printf("%d\n",test);
    printf("%s\n",test);
    printf("==============whoareyou end================\n");
}

void main(){

    char str1[] = "My String";
    char *str2 = "My String";

    printf("str1 = %s\n" ,str1);
    printf("str2 = %s\n",str2);

    str1[0] = 'X';
    //str2[0] = 'X';


    // %s 라는 서식문자는 str1 0 번째배열에서 \0널문자까지 출력된다.
    // %s 라는 서식문자는 0번째 주속.... \0주소까지 출력된다.
    printf("str1 = %s\n",str1);
    printf("str2 = %s\n",str2);

    printf("&str1[0] %d\n", &str1[0]);
    printf("str2 %d\n",str2);
    whoareyou(str1);
}