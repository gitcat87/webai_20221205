package myjava;

import java.util.Scanner;

public class ex03 {
public static void main(String[] args) {
	//�Է� :: �迭�� ũ��, ������ ����(v), �迭����
	// ���:: �迭���� �� v
	
	//1. ���� �Է��� �޽��ϴ�.
	Scanner sc =new Scanner(System.in);
	int n= sc.nextInt(); //n:: �迭�� ũ��
	int v= sc.nextInt(); //v: ������ ����
	int arr[] = new int[n]; //n���� ũ�� ��ŭ �迭�� �����մϴ�.
	for(int i=0;i<n;i++) {
		arr[i]=sc.nextInt(); // arr�� i��° �迭�� ���������� �Է�
	}
	
	//2. �ٷ� ���ϰ�, �ٷ� ���
	for(int i=0;i<n;i++) {
		if(arr[i]<v) { // "���� ��ġ�� �迭���� v���� �۴ٸ�
			System.out.print(arr[i]+" ");
		}
	}
	System.out.println();
}
}
