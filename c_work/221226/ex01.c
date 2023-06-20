#include <stdio.h>

int main(){

    int num = 10;
    int *ptr = &num;
    int **dptr = &ptr;

    printf("======= num의 값 =======\n");
    printf("num = %d\n",num);

    printf("======= num의 주소값 ========\n");
    printf("&num = %d\n",&num);
    printf("&ptr = %d\n",ptr);

    printf("======= ptr의 주소값 ========\n");
    printf("&ptr = %d\n",&ptr);
    printf("&dptr = %d\n",dptr);

    num = 20;
    printf("======= num 값 ========");
    printf("&num = %d\n",num);
    printf("*ptr = %d\n", *ptr);
    printf("**dptr = %d\n",**dptr);

    *ptr = 30;
    printf("======= num 값 ========");
    printf("&num = %d\n",num);
    printf("*ptr = %d\n", *ptr);
    printf("**dptr = %d\n",**dptr);

    **dptr = 40;
    printf("======= num 값 ========");
    printf("&num = %d\n",num);
    printf("*ptr = %d\n", *ptr);
    printf("**dptr = %d\n",**dptr);


    return 0;



}