#include <stdio.h>
#include<stdlib.h>
int money1(int a) {
	if (a == 0)
		return 0;
	else if (a <= 1)
		return 5000000;
	else if (a <= 3)
		return 3000000;
	else if (a <= 6)
		return 2000000;
	else if (a <= 10)
		return 500000;
	else if (a <= 15)
		return 300000;
	else if (a <= 21)
		return 100000;
	else
		return 0;
}
int money2(int b) {
	if (b == 0)
		return 0;
	else if (b <= 1)
		return 5120000;
	else if (b <= 3)
		return 2560000;
	else if (b <= 7)
		return 1280000;
	else if (b <= 15)
		return 640000;
	else if (b <= 31)
		return 320000;
	else
		return 0;
}

int main() {
	int *p;
	int t,a,b,sum;
	scanf("%d", &t);
	p = (int*)malloc(sizeof(int)*t);
	for (int i = 0; i < t; i++) {
		scanf("%d %d", &a, &b);
		sum = money1(a) + money2(b);
		*(p + i) = sum;
	}
	for (int i = 0; i < t; i++) {
		printf("%d\n", *(p + i));
	}
	free(p);
	return 0;
}
