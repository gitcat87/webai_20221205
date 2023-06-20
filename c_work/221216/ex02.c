#include <stdio.h>

int main(){

    //값표현은 x[0,or 1, or 3] 또는 *x(변수 앞에 별표)
    //주소값 표현은 &x 또는 변수 자체를 입력
 
    int arr1[3] = {10,20,30};
    double arr2[3] = {1.1,2.2,3.3};

    printf("arr1[0] = %d\t arr2[0] = %g\n",arr1[0],arr2[0]);
    printf("*arr1 = %d\t  *arr= %g\n",*arr1,*arr2);

    arr1[0] +=100;
    *arr2 +=100;

    printf("arr1[0] = %d\t  arr2[0] = %g\n",arr1[0],arr2[0]);
    printf("*arr1 = %d\t *arr2 = %g\n",*arr1,*arr2);
}