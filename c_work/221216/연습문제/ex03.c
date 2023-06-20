#include<stdio.h>

int main() {
	int num;
	printf("정수를 입력해주세요\n");
	scanf("%d", &num);

	printf("10진수 : %d\n", num); // 서식문자 : %d
	printf("8진수 : %o\n", num); // 서식문자 : %o 
	printf("16진수(소문자) : %x\n", num); // 서식문자 : %x
	printf("16진수(대문자) : %X\n", num); // 서식문자 : %X
	
	printf("8진수(표기) : %#o\n", num); // 서식문자 : %#o
	printf("16진수(표기) : %#x\n", num); // 서식문자 : %#x

	printf("8진수(8자리까지 0으로 채움) : %0.8o\n", num); // 서식문자 : %0.8o
	printf("16진수(8자리까지 0으로 채움) : %0.8x\n", num); // 서식문자 : %0.8x
}