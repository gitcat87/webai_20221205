package myjava;

import java.util.Random;
import java.util.Scanner;

public class ex02 {
	public static void main(String[] args) {
		//입력 : 배열의 크기, 배열값들, 임의의 숫자
		// 출력 : 배열값들 중 v와 같은 숫자인 갯수
		
		// 1. 3가지 순차적으로 입력
		Scanner sc = new Scanner(System.in);
		Random rd=new Random();
		
		int n= sc.nextInt(); //배열의 크기 숫자를 받습니다
		int arr[]=new int [n]; //arr의 크기는 n
		for(int i=0;i<n;i++) {
			arr[i] =rd.nextInt(2)+1; //i번째 배열의 값 입력
		}
		int v=sc.nextInt(); //v: 임의의 숫자
		
		// 2. 연산 :: arr와 같은 숫자의 값의 갯수
		int cnt =0;
		for(int i=0; i<n;i++) {
			if(arr[i]==v) {cnt++;}
		}
		for(int i=0;i<n;i++) {
			System.out.print(arr[i]+" ");
		}
		System.out.println();
		System.out.println(cnt);
	}
}
