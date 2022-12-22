#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(void) {
    int arr[1001];
    arr[1] = 1;
    arr[2] = 2;
    int i;
    int x;
    scanf("%d",&x);
    for (int i = 3; i <=x; i++) {
        arr[i] = (arr[i - 1] + arr[i - 2]) % 10007;
    }
    printf("%d", arr[x]);
}