#include <stdio.h>

int main(void)
{
    int i, j;
    int gugudan[10][10]; 

    for (i = 1; i <= 9; i++){
        for (j = 2; j <= 9; j++)
        {
            gugudan[i][j] = i * j;
            printf("%d X %d = %2d  ", j, i, gugudan[i][j]);        
        }
        printf("\n");
        
    }

    return 0;
}

