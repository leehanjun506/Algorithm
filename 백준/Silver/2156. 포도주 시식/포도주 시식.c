#define _CRT_SECURE_NO_WARNINGS
#define MAX(a, b) (((a) > (b)) ? (a) : (b))

#include<stdio.h>
int main() {
	int a = 0;
	scanf("%d", &a);
	int arr[10001] = { 0, };
	int arr2[3][10001] = { 0, };
	for (int i = 0; i < a; i++) {
		scanf("%d", &arr[i]);
	}
	int max = 0;
	if (a == 1)
		printf("%d", arr[0]);
	else if (a == 2)
		printf("%d", arr[0] + arr[1]);
	else {
		arr2[0][1] = arr[0];
		arr2[1][1] = arr[1];
		arr2[2][1] = arr[0] + arr[1];


		for (int j = 2; j < a; j++) {
			arr2[0][j] = MAX(arr2[2][j - 1], arr2[1][j - 1]);
			arr2[0][j] = MAX(arr2[0][j], arr2[0][j - 1]);
			arr2[1][j] = arr[j] + arr2[0][j - 1];
			arr2[2][j] = arr[j] + arr2[1][j - 1];
		}
		max = MAX(arr2[0][a - 1], arr2[1][a - 1]);
		max = MAX(max, arr2[2][a - 1]);
		printf("%d", max);
			
	}
}