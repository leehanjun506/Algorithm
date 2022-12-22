#include<stdio.h>

int main(void) {
	int a;
	int b = 0;
	for (int i = 0; i < 5; i++) {
		scanf("%d", &a);
		if (a < 40) {
			a = 40;
		}
		b += a;
	}
	printf("%d", b / 5);
	return 0;
}
