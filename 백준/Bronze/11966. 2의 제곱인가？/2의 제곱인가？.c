#include<stdio.h>

int main(void) {
	int a;
	scanf("%d", &a);
	while (1) {
		if (a % 2 == 0) {
			a = a / 2;
		}
		else if (a == 1) {
			printf("1");
			break;
		}
		else {
				printf("0");
				break;
		}
		if (a == 1) {
			printf("1");
			break;
		}	
	}
	return 0;
}