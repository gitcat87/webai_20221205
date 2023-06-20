#include <stdio.h>

int main(){
    double total=0.0, input=0.0;
    int num =0;

    for(; input>=0.0;){

        total+=input;
        printf("실수 입력: (마이너스 입력시 종료)");
        scanf("%lf",&input);
        num++;
    }

    printf("평균 = %f\n",total/(num-1));
    return 0;
}
