#include<stdio.h>
int main(void){
    int a,b,c;
    scanf("%d%d",&a,&b);
    int *p=(int*)malloc(sizeof(int)*a);
    for(int i=0;i<a;i++){
        scanf("%d",&c);
        p[i]=c;
    }
    for(int i=0;i<a;i++){
        if(p[i]<b){
            printf("%d ",p[i]);
        }
    }
    return 0;
}