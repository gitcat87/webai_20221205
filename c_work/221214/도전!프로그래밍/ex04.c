#include <stdio.h>
int main()
{
    int n1, n2, i, gcd;
    
    printf("두 정수를 입력: ");
    scanf("%d %d", &n1, &n2);
    
    for(i=1; i <= n1 && i <= n2; ++i)
    {
        if(n1%i==0 && n2%i==0)
            gcd = i;
    }
    
    printf("%d 와 %d의 최대 공약수: %d\n", n1, n2, gcd);
    
    return 0;
}
