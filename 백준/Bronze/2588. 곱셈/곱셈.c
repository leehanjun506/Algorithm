#include<stdio.h>
int main(void) {
    int a, b, c, d, e, f;
    scanf("%1d%1d%1d", &a, &b, &c);
    scanf("%1d%1d%1d", &d, &e, &f);
    printf("%d\n", (100 * a + 10 * b + c) * f);
    printf("%d\n", (100 * a + 10 * b + c) * e);
    printf("%d\n", (100 * a + 10 * b + c) * d);
    printf("%d", (100 * a + 10 * b + c) * f + (100 * a + 10 * b + c) * 10*e + (100 * a + 10 * b + c) * 100*d);
    return 0;

}
