#include <stdio.h>

int main(){
    double num = 3.14;
    double *ptr = &num;
    double **dptr = &ptr;

    printf("num = %8g\n",num); //%8g는 라인 맞추기
    printf("&num = %d\n",&num);
    printf("");
    printf("ptr = %d\n",ptr);
    printf("*ptr = %7g\n",*ptr);
    printf("&ptr = %d\n",&ptr);
    printf("\n");
    printf("dptr = %d\n",dptr);
    printf("*dptr = %d\n",dptr);
    printf("**dptr = %6g\n",dptr);
    
    

}