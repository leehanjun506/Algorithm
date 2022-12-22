#include<stdio.h>
#include<math.h>
int main(void){
    int a,b,c,s,x,count;
    int arr[10];
    scanf("%d",&a);
    scanf("%d",&b);
    scanf("%d",&c);
    s=a*b*c;
    for(int i=0;i<10;i++){
        if(s/(int)pow(10,i)==0){
            x=i;
        break;}
  arr[i]=s/(int)pow(10,i)%10;      
    }
    for(int j=0;j<10;j++){
        count=0;
        for(int k=0;k<x;k++){
            if(arr[k]==j)
                count++;
        }
        printf("%d\n",count);
        }
    return 0;
    }
