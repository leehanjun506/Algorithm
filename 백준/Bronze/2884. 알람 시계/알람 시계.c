#include<stdio.h>
int main(void) {
	int a, b;
	scanf("%d%d", &a, &b);
	if (a != 0) {
		if (b >= 45)
			printf("%d %d", a, b - 45);
		else
			printf("%d %d", a - 1, 15 + b);
	}
	if (a == 0) {
		if (b >= 45)
			printf("%d %d", a, b-45);
		else
			printf("23 %d", 15 + b);

	}
	return 0;

}