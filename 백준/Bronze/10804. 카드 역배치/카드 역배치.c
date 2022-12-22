#include<stdio.h>

int main(void) {
	int c[20] = { 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 };
	int a, b;
	for (int i = 0; i < 10; i++) {
		scanf("%d%d", &a, &b);
		for (int j = 0; j < (b - a + 1) / 2; j++) {
			int temp = c[a-1+j];
			c[a-1+j] = c[b - j - 1];
			c[b - j - 1] = temp;
		}
	}
	for (int k = 0; k < 20; k++) {
		printf("%d ", c[k]);
	}
	return 0;
}
