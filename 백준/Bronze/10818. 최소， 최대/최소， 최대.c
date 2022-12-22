#include<stdio.h>
#include<stdlib.h>
int main(void) {
    int* a;
    int array, input;
    int max, min;
    scanf("%d", &array);
    a = (int*)malloc(array * sizeof(int));
    for (int i = 0; i < array; i++) {
        
        scanf("%d", &a[i]);
    }
    if (array == 1) {
        printf("%d %d", a[0],a[0]);
        free(a);
        return 0;
    }
    if (a[1] > a[0]) {
        max = a[1];
        min = a[0];
    }
    else {
        max = a[0];
        min = a[1];
    }
    
    for (int i = 0; i < array; i++) {
        if (a[i] > max) {
            max = a[i];
        }
        else {
            if (a[i] < min) {
                min = a[i];
            }
        }
        
    }
    printf("%d %d", min, max);
    
    free(a);
    return 0;
}