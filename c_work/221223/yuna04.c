#include <stdio.h>

int main(){
    //아스키코드, 배열
    //이름 입력받고, 이름에 있는 철자들 순서대로 출력하기

    // 1. 이름입력 받기
    char name[20];
    printf("이름을 입력해주세요.  "); 
    scanf("%s", &name);    
   

    // 2. 배열 생성
    
    // 배열값이 0이면 "이 철자가 나타나지 않음"
    // 배열값이 1 이상이면 "이 철자가 나타났음"
    int count[26] = {0};

    // 예시)count[0]의 배열값이 0이라면 A가 미출현
    // 예시계속)count[2]의 배열값이 2라면 C가 출현

    // 3. name 탐색
    for(int i =0;i<sizeof(name);i++){
        // 소문자만 입력받는다고 가정할 때
        count[name[i] - 'a']++;

        // 입력값이 leeyuna라고 가정할때
        // 첫 입력값이 name[6] = a, count['a'-'a']++ -> count[0]++
        // name[1]=e, count['e'-'e']++ -> count[4]++

    }
    printf("나타나는 알파벳은 아래와 같습니다.\n");
    for(int i=0; i < 26; i++){
        if(count[i]>0){
            printf("%c", i+'a');
        }
    }
}