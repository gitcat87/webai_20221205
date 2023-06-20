#include <stdio.h>

int a, b;
char c;

int main()
{
    printf("두 개의 숫자와 처리할 연산자를 적어주세요(+,-,/,*)");
    scanf("%d", &a);
    scanf("%d", &b);
    scanf(" %c", &c);

    printf("첫번째 입력한 숫자 : %d\n", a);
    printf("두번째 입력한 숫자 : %d\n", b);
    printf("입력한 연산자 : %c\n", c);

    if (c == '+')
    {
        printf("%d %c %d = %d\n", a, c, b, (a + b));
    }
    else if (c == '-')
    {
        printf("%d %c %d = %d\n", a, c, b, (a - b));
    }
    else if (c == '/')
    {
        printf("%d %c %d = %d\n", a, c, b, (a / b));
    }
    else if (c == '*')
    {
        printf("%d %c %d = %d\n", a, c, b, (a * b));
    }
    else
    {
        printf("사칙연산자만 적어주세요!\n");
        printf("계산에 실패했습니다.");
    }

    return 0;
}