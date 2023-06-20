#include <stdio.h>

int main(void)
{
	int num, i;
	int cnt = 0;

	for (num = 2; cnt < 10 ; num++)
		for (i = 1; i < num; i++)
		{
			if (num % i == 0 && i != 1)
				break;
			if (i == num - 1)
			{
				printf("%d ", num);
				cnt++;
			}
		}

	return 0;
}