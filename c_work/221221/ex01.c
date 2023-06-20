/*
    page 268
    2. char형 배열에 지정한뒤 문자열을 역순으로
    3. LOVE라는 단어를 입력받아 아스키 보드값중 가장 큰 값인 V를 출력하자

    page 284

    포인터 문제

    문제 1
    아래의 예제 실행시 변수와 포인터 변수의 관계를 그림을 그려서 설명해보자
    int main(){

        int num = 10;
        int *ptr = &num;
        int *ptr2 = ptr1;
    }

    (*ptr1)++;
    (*ptr2)++;
    printf("%d \n",num);

    문제 2

    int형 변수 num1과 num2를 선언과 동시에 각각 10과 20으로 초기화하고

*/

#include <stdio.h>

int main(){

    char str[] = "LOVE";
    int max = str[0];

    printf("str = %s\n",str);
    for ( int i = 0 ; i < 5 ; i++){
        printf("str[%d] =%d\n",i,str[i]);
        if (max < str[i]){
            max =str[i];
        }
    }
    printf("max = %c",max);

    return 0;
}