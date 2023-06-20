#include <stdio.h>


    //가장 큰 수 반환
    int retbvalue(int a, int b, int c){
        if (a > b)
        {
            if( a > c){
                return a;
            }else{
                return b;}
        }
        else{
            if(b > c){
                
            }if( b > a ){
                return b;
            }else{ return c;}
        }

    }
    //가장 작은 수 반환
    int retsvalue(int a, int b, int c){
        
        if( a < b){
            if(b < c){
                return a;
            }else {
                return b;
            }
        }
        else{
            if(b < a){
                if(c < b)
                    return b;
            }
                else{
                    return c;            
            }
        }       
    }

int main(){
    printf("%d\n",retbvalue(5,10,3));
    printf("%d\n",retbvalue(5,10,3));
    printf("%d\n",retbvalue(5,10,3));
    printf("%d\n",retbvalue(5,10,3));
    printf("%d",retsvalue(5,10,3));
}