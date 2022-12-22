#include<stdio.h>

int main(void) {
	int a,c;
	int b = 1;
	scanf("%d", &a);
	c = a;
	for (int i = 0; i < a; i++) {
		if (i >= 1) {
			printf("\n");
		}
		while (b < c) {
			printf(" ");
			b++;
			
		}
		 b = 1;
		 c--;
	for (int j = 0; j < i+1; j++) {
			
			printf("*");
		}
	
	}
	return 0;
}