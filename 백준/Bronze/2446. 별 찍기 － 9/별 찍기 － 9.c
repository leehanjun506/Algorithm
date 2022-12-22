#include<stdio.h>

int main(void) {
	int a,b,c;
	scanf("%d", &a);
	for (int i = 1; i < a+1; i++) {
		for (int j = 1; j < 2*a; j++) {
			if (j - i >= 0 && i+j<2*a+1)
				printf("*");
			else if(j - i < 0)
				printf(" ");
			
			
		}
		printf("\n");	
			
	}
	for (int k = 1; k < a; k++) {
		for (int z = 1; z < 2 * a; z++) {
			if (k + z >= a && z - k < a+1)
				printf("*");
			else if(k + z < a)
				printf(" ");
		}
		printf("\n");
	}
	return 0;
}