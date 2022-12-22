#include <stdio.h>
int main(void) {
	int n,num,c;
	scanf("%d", &n);
	num = n / 5;
	c = n % 5;
	if (c == 0) {
		printf("%d", num);
		return 0;
	}
	for (num; num > 0; num--) {
		if (c % 3 == 0) {
			printf("%d", (c / 3) + num);
			return 0;
		}
		c = c + 5;
	}
	if (n % 3 == 0) {
		printf("%d", n / 3);
		return 0;
	}
	printf("%d", -1);
	return 0;
}
