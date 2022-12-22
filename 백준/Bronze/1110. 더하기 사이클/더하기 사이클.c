#include<stdio.h>

int main() {
	int a, b, c, sum, d, t;
	int i = 0;
	scanf("%d", &a);
    if(a<10)
        a = 10*a;
	d = a;
	t = a;
	do {
        a = d;
		b = a / 10;
		c = a % 10;
		sum = b + c;
		d = c * 10 + sum % 10;

		i++;
	} while (t != d);
	printf("%d", i);
	return 0;
}