package myjava;

import java.util.Random;
import java.util.Scanner;

public class ex02 {
	public static void main(String[] args) {
		//�Է� : �迭�� ũ��, �迭����, ������ ����
		// ��� : �迭���� �� v�� ���� ������ ����
		
		// 1. 3���� ���������� �Է�
		Scanner sc = new Scanner(System.in);
		Random rd=new Random();
		
		int n= sc.nextInt(); //�迭�� ũ�� ���ڸ� �޽��ϴ�
		int arr[]=new int [n]; //arr�� ũ��� n
		for(int i=0;i<n;i++) {
			arr[i] =rd.nextInt(2)+1; //i��° �迭�� �� �Է�
		}
		int v=sc.nextInt(); //v: ������ ����
		
		// 2. ���� :: arr�� ���� ������ ���� ����
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
