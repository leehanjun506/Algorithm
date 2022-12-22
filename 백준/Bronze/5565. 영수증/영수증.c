#include<stdio.h>
int main(void) {
	int n=9;
	int sum;
	int a;
	scanf("%d",&sum);
	for (int i = 0; i < n; i++) {
		scanf("%d",&a);
		sum -= a;
	}
	printf("%d", sum);
	return 0;
}