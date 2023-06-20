/*
    the differnce of 
    call by reference between
    call by value
*/

#include <stdio.h>
// call by value
void whovalue(int value){
    value = 20;
    printf("value = %d\n",value);
}

void whoref(int *reference){
    *reference = 20;
    printf("*reference = %d\n",*reference);
}
// call by reference
void main(){
    int a = 10;
    printf("a =%d\n",a);
    whovalue(a);
    printf("a =%d\n",a);
    whoref(&a);
    printf("a =%d\n",a);
}
