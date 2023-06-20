#include <stdio.h>
int main(void)
{
    int korea[4], i;
    for(i=0;i<4;i+=1)
    {
        printf("%d번째 득점수 입력 :", i);
        scanf("%d", &korea[i]);
        printf("입력된 데이터 :%d\n", korea[i]);
    }
    return 0;
}