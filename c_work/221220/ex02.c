//Array라는 단어가 입력되면 길이를 계산해서 출력하자
//char형 배열에 저장한 뒤 문자열을 역순으로
//3. Love라는 단어를 입력받아 아스키 보드값중 가장 큰 값인 V를 출력

#include <stdio.h>

int main(){
    char str[100];
    int len; //길이 구하기
    printf("문자열을 입력하세요\n");
    scanf("%s",str);

    for (int i =0; i<100; i++){
        if(str[i]=='\0'){ //str에 null문자를 찾는다면
            printf("길이는:%d\n",i); //출력하고
            len = i;
            break; //중지
    }
}

    if(len%2==0){
        for (int i =0; i<5; i++){
            char temp = str[i];
            str[i] = str[len -(i+1)];
            str[len-(i+1)] = temp;
        }
    }
    else{

        
        
    }

    printf("%s\n",str);
    return 0;

}