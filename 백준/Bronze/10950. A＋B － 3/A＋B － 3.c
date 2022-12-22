#include<stdio.h>
#include<stdlib.h>
int main(void) {
    int* p;
    int array;
    int b, c;
    scanf("%d", &array);
    p = (int*)malloc(sizeof(int) * array);
    for (int i = 0; i < array; i++) {
        scanf("%d %d", &b, &c);
        *(p+i) = b + c ;
    }
    for (int i = 0; i < array; i++) {
        printf("%d\n", p[i]);
    }
    free(p);
    return 0;
}