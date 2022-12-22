#include<stdio.h>

int main(void) {
	int a;
	scanf("%d", &a);
	for (int i = 0; i < a; i++) {
		if(i>=1)
			printf("\n");
		for (int j = 0; j < i+1; j++) {
			printf("*");
		}
	
	}
	return 0;
}