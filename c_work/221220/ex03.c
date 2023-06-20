#include <stdio.h>

int sfunc(int num){
    num = 30;
    printf("num = %d\n",num);
    return num; 
}

int main(){
    int age = 20;
    age = sfunc(age); //void sfunc(int num = age)
    printf("age = %d\n",age);
    return 0;
}