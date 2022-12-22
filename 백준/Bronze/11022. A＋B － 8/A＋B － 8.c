#include<stdio.h>
#include<stdlib.h>
struct input {
    int q;
    int w;
    int e;
};
int main(void) {
    struct input *p;
    
    int b, c;
    int arr;
   
    scanf("%d", &arr);

    p = (struct input*)malloc(sizeof(struct input) * arr);
    for (int i = 0; i < arr; i++) {
        scanf("%d%d", &b, &c);
        p[i].q = b + c;
        p[i].w = b;
        p[i].e = c;
    }
    for (int i = 0; i < arr; i++) {
        printf("Case #%d: %d + %d = %d\n", i + 1, p[i].w, p[i].e, p[i].q);
    }
    free(p);
    return 0;
}