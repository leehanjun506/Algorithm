#include <stdio.h>

int fib(int n) {
	static int b = 0, c = 0, a = 1;
	if (n == 1) {
		printf("%d", a);
		return a;
	}
	else {
		c = a;
		a += b;
		b = c;
		fib(n - 1);
	}
}
int main()
{
	int n;

	
	scanf("%d", &n);
	fib(n);
	return 0;
	
}


