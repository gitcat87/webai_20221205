#include <stdio.h>

int main(){

    int c_cnt = 0;
    int num =1;
    int t_cnt = 0;

    while(t_cnt < 5){
        while(c_cnt>0){
            printf(" 0 ");
            c_cnt =  c_cnt-1;            
        }
        printf("  *\n ");
        c_cnt = c_cnt+num;
        num++;
        t_cnt++;
        
        
    }
    return 0;
}