#include<stdio.h>
int main(void) {
	int array[9];
	int sum=0;
	int subtract[9];
	int finish[49];
	for (int i = 0; i < 9; i++) {
		scanf("%d", &array[i]);
		sum += array[i];
	}

		for (int j = 0; j < 9; j++) {
			subtract[j] = sum - array[j];
			for (int k = 0; k < 9; k++) {
				finish[(j + 1)*(k + 1) - 1] = subtract[j] - array[k];
				if (k == j) {
					continue;
				}
				if (finish[(j + 1)*(k + 1) - 1] == 100) {
					array[j] = 100;
					array[k] = 100;
				}
			}
			if (array[j] == 100)
				break;
		}
		for (int l = 0; l < 8; l++) {
			for (int m = l + 1; m < 9; m++) {
				if (array[l] > array[m]) {
					int tmp = array[l];
					array[l] = array[m];
					array[m] = tmp;
				}
			}
			
		}
		for (int i = 0; i < 7; i++) {
			printf("%d\n", array[i]);
		}


		return 0;
	
}
