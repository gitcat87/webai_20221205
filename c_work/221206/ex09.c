#include <stdio.h>

int main(){

    int a = 10;

    a++;
    printf("a = %d\n",a);
    a--;
    printf("a = %d\n\n",a);

    printf("a = %d\n",a++); // 자료값을 먼저 보여주고 연산 값은 출력x
    printf("a = %d\n",a--);
    printf("a = %d\n\n",a);

    printf("a = %d\n",--a);
    printf("a = %d\n",++a);
    printf("a = %d\n",a);

    return 0;

}