#include <stdio.h>

int main(){
    int cnt[6] ={0};
    for(int i = 0; i <5; i++){
        int num;
        scanf("%d",&num); //제출한 사람 번호 입력
        cnt[num]++;
    }

for (int i = 1; i<=30;i++){
    if(cnt[i]==0){
        printf("미제출 학생: %d\n",i);
    }
}
}

