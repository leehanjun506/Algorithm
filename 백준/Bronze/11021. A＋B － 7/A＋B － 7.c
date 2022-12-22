#include<stdio.h>
#include<stdlib.h>
int main(void){
    int b,c;
    int *p;
    int arr;
    scanf("%d",&arr);
    p=(int*)malloc(sizeof(int)*arr);
    for(int i=0;i<arr;i++){
        scanf("%d%d",&b,&c);
        p[i]=b+c;
    }
    for(int i=0;i<arr;i++){
        printf("Case #%d: %d\n",i+1,p[i]);
    }
    free(p);
    return 0;
}